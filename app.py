import flask
import redis
from flask import Flask, request
from redis import Redis, RedisError
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf


redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)
app = Flask(__name__)

def upload(image, img):
KEYSPACE="mykeyspace_mnist"
    global f
    if request.method== "POST" :
        createKeySpace()
        f= request.files["file"]
        if not (f and allowed_file(f.filename)):
            return jsonify({"error": 1001, "msg": "请检查上传的图片类型，仅限于png、PNG、jpg、JPG、bmp"})
        basepath = os.path.dirname(__file__)  
 
        upload_path = os.path.join(basepath, secure_filename(f.filename))  
        
        f.save(upload_path)
 
        img = Image.open(upload_path)
        result=imageprepare(img)
        x = tf.placeholder(tf.float32, [None, 784])

        y_ = tf.placeholder(tf.float32, [None, 10])
        W_conv1 = weight_variable([5, 5, 1, 32])
        b_conv1 = bias_variable([32])

        x_image = tf.reshape(x,[-1,28,28,1])

        h_conv1 = tf.nn.relu(conv2d(x_image,W_conv1) + b_conv1)
        h_pool1 = max_pool_2x2(h_conv1)

        W_conv2 = weight_variable([5, 5, 32, 64])
        b_conv2 = bias_variable([64])

        h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
        h_pool2 = max_pool_2x2(h_conv2)

        W_fc1 = weight_variable([7 * 7 * 64, 1024])
        b_fc1 = bias_variable([1024])

        h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])
        h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

        keep_prob = tf.placeholder("float")
        h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

        W_fc2 = weight_variable([1024, 10])
        b_fc2 = bias_variable([10])

        y_conv=tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)

        cross_entropy = -tf.reduce_sum(y_*tf.log(y_conv))
        train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
        correct_prediction = tf.equal(tf.argmax(y_conv,1), tf.argmax(y_,1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

        saver = tf.train.Saver()

        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            saver.restore(sess, '/root/mnist/model.ckpt') 

            prediction=tf.argmax(y_conv,1)
            predint=prediction.eval(feed_dict={x: [result],keep_prob: 1.0}, session=sess)

            print('result:')
            print(predint[0])
            final=str(predint[0])
            insertdata(final)
return final

from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
cluster = Cluster(contact_points=["172.17.0.2"],port=9042)
session = cluster.connect()
session.execute("create KEYSPACE if not exists mnist_database WITH replication = {'class':'SimpleStrategy', 'replication_factor': 2};")
session.execute("use mnist_database")
session.execute("create table if not exists mnist(id uuid, digits int, image_name text, upload_time timestamp, primary key(id));")



#flask
session.execute("create KEYSPACE if not exists mnist_database WITH replication = {'class':'SimpleStrategy', 'replication_factor': 2};")
session.execute("use mnist_database")
session.execute("create table if not exists mnist(id uuid, digits int, image_name text, upload_time timestamp, primary key(id));")
@app.route("/prediction", methods=['GET','POST'])
def predictint():
    imname = request.files["file"]   
    file_name = request.files["file"].filename
    imvalu = prepareImage(imname)
    prediction = tf.argmax(y,1)
    pred = prediction.eval(feed_dict={x: [imvalu]}, session=sess)
    #get timestamp
    uploadtime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    #store history
    session.execute("INSERT INTO mnist(id, digits, image_name, upload_time) values(uuid(), %s, %s, %s)",[int(str(pred[0])), file_name, uploadtime])
    return "The number upload is: [%s]" % str(pred[0])


if __name__ == "__main__":
   def createKeySpace():
       cluster = Cluster(contact_points=['127.0.0.1'],port=9042)
       session=cluster.connect()
   app.run(host='0.0.0.0',port=80,)
