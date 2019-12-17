import  sys,os,socket,threading
os.environ['path'] = os.getenv('path') + ";" + os.path.abspath('./lib')
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QVBoxLayout,QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import log.commlog as commlog
import json
import controlVoice

class MainFram(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.t1=threading.Thread(target=self.remote)
        self.t1.setDaemon(True)
        self.t1.start()

    def initUI(self):
        vbox=QVBoxLayout()
        shut=QPushButton('关机测试')
        self.txtTip=QLabel()
        shut.clicked.connect(self.shutDown)

        vbox.addWidget(shut,1,Qt.AlignLeft)
        vbox.addWidget(self.txtTip,2,Qt.AlignLeft|Qt.AlignTop)
        self.setLayout(vbox)
        self.setWindowTitle('关机插件')
        self.setWindowIcon(QIcon('./png/1.png'))
        self.setGeometry(100,100,300,300)
        self.showMinimized()
        # self.show()

    def remote(self):
        # 创建socket对象
        s = socket.socket()
        try:
            s1= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s1.connect(('8.8.8.8', 80))
            ip = s1.getsockname()[0]
            print(ip)
        except Exception as e:
            print(e.args)
        finally:
            s1.close()
        # 将socket绑定到本机IP和端口
        s.bind((ip, 8000))
        # 服务端开始监听来自客户端的连接
        s.listen()
        commlog.logger.info('等待连接...')
        print('等待连接...')
        while True:
            # 每当接收到客户端socket的请求时，该方法返回对应的socket和远程地址
            c, addr = s.accept()
            print('连接地址：', addr)

            commlog.logger.info("{} {}".format('连接地址：',addr))
            # c.send('您好，您收到了服务器的新年祝福！'.encode('utf-8'))
            # 关闭连接
            try:
                content = c.recv(1024).decode('utf-8')
                jsondata=json.loads(content)
                req_type=jsondata['type']
                commlog.logger.info("{}{}".format('收到命令:',content))
                if req_type=='cmd':
                    recdata=jsondata['data']
                    os.system(recdata)
                elif req_type=='sysvoice':
                    c = controlVoice.ControlVoice()
                    recdata = jsondata['data']
                    if recdata=='addvoice':
                        c.addVoice()
                    elif recdata=='minusvoice':
                        c.minusVoice()
                    elif recdata=='mutevoice':
                        c.muteVoice()
            except Exception as e:
                print(e)

            c.close()

    def closeEvent(self, e):
        print("窗口关闭")

    def shutDown(self):
        self.txtTip.setText("shut down")
        commlog.logger.info('test shutdown')
        os.system('shutdown -s -f -t 00')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # ex = Example()
    f=MainFram()
    sys.exit(app.exec_())
