# _*_ coding:utf-8 _*_
# developer: wangsheng
# develop_time: 2020/2/18 12:35
# file_name: test
# develop_IDE: PyCharm
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def tensorflow_demo():
    """
    TensorFlow的基本结构
    :return:
    """
    # 原生python加法运算
    a = 2
    b = 3
    c = a + b
    print("普通加法运算的结果：", c)

    # TensorFlow实现加法运算
    g = tf.Graph()
    with g.as_default():        # 构建图
        a_t = tf.constant(2, name="a_t")
        b_t = tf.constant(3, name="b_t")
        # c_t = a_t + b_t
        c_t = tf.add(a_t, b_t,name="c_t")
        # print("a_t的图属性:", a_t.graph)
        print(c_t)
        print("Tensorflow加法运算的结果：", c_t)

    # 开启会话
    with tf.Session(graph=g) as sess:
        c_t_value = sess.run(c_t)
        print("c_t_value:", c_t_value)
        # 将图写入本地
        tf.summary.FileWriter("./tmp/summary", graph=sess.graph)


def linear_regression():
    """
    自实现一个线性回归
    :return:
    """
    with tf.variable_scope("prepare_date"):
        # 准备数据
        x = tf.random_normal(shape=[100, 1], name="feature")
        y_true = tf.matmul(x, [[0.8]]) + 0.7

    with tf.variable_scope("create_model"):
        # 构造模型
        #   定义模型参数 用 变量
        weights = tf.Variable(initial_value=tf.random_normal(shape=[1, 1]), name="weights")
        bias = tf.Variable(initial_value=tf.random_normal(shape=[1, 1]), name="bias")
        y_predict = tf.matmul(x, weights) + bias

    with tf.variable_scope("loss_function"):
        # 构造损失函数
        error = tf.reduce_mean(tf.square(y_predict - y_true))

    with tf.variable_scope("optimize"):
        # 优化损失
        optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(error)

    # 收集变量
    tf.summary.scalar("error", error)
    tf.summary.histogram("weights", weights)
    tf.summary.histogram("bias", bias)

    # 合并变量
    merged = tf.summary.merge_all()

    # 创建Saver对象
    saver = tf.train.Saver()

    # 显式地初始化变量
    init = tf.global_variables_initializer()

    # 开启会话
    with tf.Session() as sess:
        # 初始化变量
        sess.run(init)

        # 创建事件文件夹
        file_writer = tf.summary.FileWriter("./tmp/linear", graph=sess.graph)

        # 查看初始化模型参数之后地值
        print("训练前模型参数为：权重%f，偏置%f，损失%f" % (weights.eval(), bias.eval(), error.eval()))

        # 开始训练
        # for i in range(100):
        #     sess.run(optimizer)
        #     print("第%d次训练后模型参数为：权重%f，偏置%f，损失%f" % (i+1, weights.eval(), bias.eval(), error.eval()))
        #
        #     # 运行合并变量操作
        #     summarry = sess.run(merged)
        #
        #     # 将每次迭代后的变量写入事件文件
        #     file_writer.add_summary(summarry, i)
        #
        #     # 保存模型
        #     if i % 10 == 0:
        #         saver.save(sess, "./tmp/model/my_linear.ckpt")

        # 加载模型
        if os.path.exists("./tmp/model/checkpoint"):
            saver.restore(sess, "./tmp/model/my_linear.ckpt")

        print("训练后模型参数为：权重%f，偏置%f，损失%f" % (weights.eval(), bias.eval(), error.eval()))


# 1)定义命令行参数
tf.app.flags.DEFINE_integer("max_step", 100, "训练模型的步数")
tf.app.flags.DEFINE_string("model_dir", "Unknown", "模型保存的路径+模型名字")
# 2)简化变量名
FLAGS = tf.app.flags.FLAGS

def command_demo():
    """
    命令行参数演示
    :return:
    """
    print("max_step:", FLAGS.max_step)
    print("model_dir:", FLAGS.model_dir)

def main(argv):
    print(argv)

# tensorflow_demo()
linear_regression()
# command_demo()
# tf.app.run()        # 启动main函数
