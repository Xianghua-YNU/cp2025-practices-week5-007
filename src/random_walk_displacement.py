import numpy as np
import matplotlib.pyplot as plt

def random_walk_displacement(num_steps, num_simulations):
    """
    模拟随机行走并返回每次模拟的最终位移

    参数:
    num_steps (int): 随机行走的步数
    num_simulations (int): 模拟的次数

    返回:
    list: 包含每次模拟最终位移的列表
    """
    final_displacements = np.random.choice([-1,1],size=(2,num_simulations, num_steps)).sum(axis=2)

    return final_displacements

def plot_displacement_distribution(final_displacements, bins=30):
    """
    绘制位移分布直方图

    参数:
    final_displacements (list): 包含每次模拟最终位移的列表
    bins (int): 直方图的组数
    """
    displacements = np.sqrt(final_displacements[0]**2+final_displacements[1]**2)
    plt.hist(displacements, bins=bins, density=True, alpha=0.7, color='b')
    plt.title('Random Walk Displacement Distribution')
    plt.xlabel('Final Displacement')
    plt.ylabel('Probability Density')
    plt.grid(True)
    plt.show()

def plot_displacement_square_distribution(final_displacements, bins=30):
    """
    绘制位移分布直方图

    参数:
    final_displacements (list): 包含每次模拟最终位移的列表
    bins (int): 直方图的组数
    """
    displacements_square = final_displacements[0]**2+final_displacements[1]**2
    plt.hist(displacements_square, bins=bins, density=True, alpha=0.7, color='b')
    plt.title('Random Walk Displacement Square Distribution')
    plt.xlabel('Final Displacement Square')
    plt.ylabel('Probability Density')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # 可调整的参数
    num_steps = 1000  # 随机行走的步数
    num_simulations = 1000  # 模拟的次数
    bins = 30  # 直方图的组数

    # 模拟随机行走
    displacements = random_walk_displacement(num_steps, num_simulations)

    # 绘制位移分布直方图
    plot_displacement_distribution(displacements, bins)
    
    # 绘制位移平方分布直方图
    plot_displacement_square_distribution(displacements, bins)
