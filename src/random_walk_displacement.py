import numpy as np
import matplotlib.pyplot as plt

def random_walk_displacement(num_steps, num_simulations):
    """
    模拟随机行走并返回每次模拟的最终位移

    参数:
    num_steps (int): 随机行走的步数
    num_simulations (int): 模拟的次数

    返回:
    numpy.ndarray: 形状为(2, num_simulations)的数组，表示每次模拟的最终位移
    """
    # 检查输入参数的有效性
    if not isinstance(num_steps, int) or num_steps <= 0:
        raise ValueError("num_steps必须是正整数")
    if not isinstance(num_simulations, int) or num_simulations <= 0:
        raise ValueError("num_simulations必须是正整数")

    # 生成随机步长（x和y方向）
    steps = np.random.choice([-1, 1], size=(2, num_simulations, num_steps))
    
    # 对步数维度求和得到最终位移
    final_displacements = np.sum(steps, axis=2)
    
    return final_displacements

def plot_displacement_distribution(final_displacements, bins=30):
    """
    绘制位移分布直方图

    参数:
    final_displacements (numpy.ndarray): 形状为(2, N)的数组，包含每次模拟的最终位移
    bins (int): 直方图的组数
    """
    # 计算每次模拟的最终位移r
    x = final_displacements[0]
    y = final_displacements[1]
    r = np.sqrt(x**2 + y**2)
    
    # 绘制直方图
    plt.figure(figsize=(10, 6))
    plt.hist(r, bins=bins, density=True, alpha=0.6, color='g')
    plt.title("最终位移分布")
    plt.xlabel("位移 r")
    plt.ylabel("概率密度")
    plt.show()

def plot_displacement_square_distribution(final_displacements, bins=30):
    """
    绘制位移平方分布直方图

    参数:
    final_displacements (numpy.ndarray): 形状为(2, N)的数组，包含每次模拟的最终位移
    bins (int): 直方图的组数
    """
    # 计算位移平方r²
    x = final_displacements[0]
    y = final_displacements[1]
    r_squared = x**2 + y**2
    
    # 绘制直方图
    plt.figure(figsize=(10, 6))
    plt.hist(r_squared, bins=bins, density=True, alpha=0.6, color='b')
    plt.title("位移平方分布")
    plt.xlabel("r²")
    plt.ylabel("概率密度")
    plt.show()

if __name__ == "__main__":
    # 可调整的参数
    num_steps = 1000    # 随机行走的步数
    num_simulations = 1000  # 模拟的次数
    bins = 30           # 直方图的组数

    # 获取模拟结果
    final_displacements = random_walk_displacement(num_steps, num_simulations)
    
    # 绘制位移分布
    plot_displacement_distribution(final_displacements, bins)
    
    # 绘制位移平方分布
    plot_displacement_square_distribution(final_displacements, bins)
