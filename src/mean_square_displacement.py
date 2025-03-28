import numpy as np
import matplotlib.pyplot as plt

def random_walk_finals(num_steps=1000, num_walks=1000):
    """生成多个二维随机游走的终点位置
    
    通过模拟多次随机游走，每次在x和y方向上随机选择±1移动，
    计算所有随机游走的终点坐标。

    参数:
        num_steps (int, optional): 每次随机游走的步数. 默认值为1000
        num_walks (int, optional): 随机游走的次数. 默认值为1000
        
    返回:
        tuple: 包含两个numpy数组的元组 (x_finals, y_finals)
            - x_finals: 所有随机游走终点的x坐标数组
            - y_finals: 所有随机游走终点的y坐标数组
    """
    x_finals = np.zeros(num_walks)
    y_finals = np.zeros(num_walks) #定义空数组存储坐标
    for i in range(num_walks):    #以游走次数设定循环次数
        x_finals[i] = np.sum(np.random.choice([-1,1],num_steps)) #生成一千个随机值为±1的值并求和
        y_finals[i] = np.sum(np.random.choice([-1,1],num_steps))
    return (x_finals,y_finals)


def calculate_mean_square_displacement():
    """计算不同步数下的均方位移
    
    对于预设的步数序列[1000, 2000, 3000, 4000]，分别进行多次随机游走模拟，
    计算每种步数下的均方位移。每次模拟默认进行1000次随机游走取平均。
    
    返回:
        tuple: 包含两个numpy数组的元组 (steps, msd)
            - steps: 步数数组 [1000, 2000, 3000, 4000]
            - msd: 对应的均方位移数组
    """
    steps = np.array([1000,2000,3000,4000]);msd = []    #定义步数数组,均方位移数组
    for i in steps:
        x,y = np.array(random_walk_finals(num_steps = i))   #获取对应步数的位移
        msd.append(np.mean(x**2 + y**2))        #计算位移平方并求均值
    return (steps,msd)


def analyze_step_dependence():
    """分析均方位移与步数的关系，并进行最小二乘拟合
    
    返回:
        tuple: (steps, msd, k)
            - steps: 步数数组
            - msd: 对应的均方位移数组
            - k: 拟合得到的比例系数
    """
    steps,msd = calculate_mean_square_displacement()    #获取步数，均方位移
    k = np.sum(steps * msd) / np.sum(steps**2)          #求出比例系数
    return (steps,msd,k)


if __name__ == "__main__":
    steps,msd,k = analyze_step_dependence()
    stepsx = np.linspace(steps[0], steps[-1],1000)
    msdy = k*stepsx
    fig = plt.figure()
    plt.scatter(steps,msd)
    plt.plot(stepsx, msdy)
    plt.xlabel('步数')
    plt.ylabel('均方位移')
    plt.title('随机行走与均方位移之间的关系')
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.savefig('随机行走与均方位移之间的关系')
    print("步数和对应的均方位移：")    #打印数据分析结果
    for i, j in zip(steps, msd):
        print(f"步数: {i:5d}, 均方位移: {j:.2f}")
    
    print(f"\n拟合结果：r² = {k:.4f}N")
    print(f"k={k:.4f}")
    print(f"与理论值k=2的相对误差: {abs(k-2)/2*100:.2f}%")
    pass
