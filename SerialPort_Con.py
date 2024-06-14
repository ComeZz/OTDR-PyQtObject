import serial
import time



class SerialPort_Con:
    # 初始化函数，用于初始化串口参数
    def __init__(self,port,baudrate,timeout):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.ser = serial.Serial(self.port,self.baudrate,timeout=self.timeout)
        
    # 发送数据函数，用于向串口发送数据
    def send(self,data):
        self.ser.write(data.encode())
        
    # 读取数据函数，用于从串口读取数据
    def read(self):
        data = self.ser.readline()
        return data.decode()
    
    # 关闭串口函数
    def close(self):
        self.ser.close()
        
    # 打开串口函数
    def open(self):
        self.ser.open()
        
    # 刷新串口函数
    def flush(self):
        self.ser.flush()
        
    # 清除串口缓存函数
    def reset_input_buffer(self):
        self.ser.reset_input_buffer()
        
    # 清除串口输出缓存函数
    def reset_output_buffer(self):
        self.ser.reset_output_buffer()
        
    # 清除串口缓存函数
    def clear(self):
        self.ser.clear()
    
    #设置通道号，并获取收到的串口值，判断是否正确
    def set_ConNumber(self,ConNumber):
        self.clear()
        self.ConNumber=ConNumber
        CON_str="<OSW_01_SW_"+"{:02d}".format(ConNumber)+">"
        self.ser.write(CON_str.encode())
        #等待返回值
        time.sleep(0.5)
        #用于校验的返回值
        ReCheck_str="<OSW_01_SW_"+"{:02d}".format(ConNumber)+"OK"+">"
        #获取收到的串口值并判断是否正确
        data=self.ser.read_all()
        if data.decode()==ReCheck_str:
            return True
        else:
            return False
        
        
        