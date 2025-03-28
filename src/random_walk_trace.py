import matplotlib.pyplot as plt
import numpy as np

def random_walk_2d(steps):
    """生成二维随机行走轨迹
     x_step = np.random.choice([-1,1],steps)
    y_step = np.random.choice([-1,1],steps)

    return(x_step.cumsum(), y_step.cumsum())
    参数:
        steps (int): 随机行走的步数
        
    返回:
        tuple: 包含x和y坐标序列的元组 (x_coords, y_coords)
    """
    # TODO: 实现随机行走算法
    # 提示：
    # 1. 使用 np.random.choice 生成随机步长 ([-1, 1])
    # 2. 分别生成x和y方向的步长序列
    # 3. 使用 cumsum() 计算累积和得到轨迹
    pass

def plot_single_walk(path):
    """绘制单个随机行走轨迹
    x_coords, y_coords = path
    
    plt.plot(x_coords, y_coords, marker='.')
    plt.scatter([x_coords[0]], [y_coords[0]], color='green', s=100, label='Start')
    plt.scatter([x_coords[-1]], [y_coords[-1]], color='red', s=100, label='End')
    plt.axis('equal')
    plt.legend()
    参数:
        path (tuple): 包含x和y坐标序列的元组
    """
    # TODO: 实现单个轨迹的绘制
    # 提示：
    # 1. 使用 plt.plot 绘制轨迹线
    # 2. 使用 plt.scatter 标记起点和终点
    # 3. 设置坐标轴比例相等
    # 4. 添加图例
    pass

def plot_multiple_walks():
    """在2x2子图中绘制四个不同的随机行走轨迹"""
     fig, axes = plt.subplots(2, 2, figsize=(12, 12))
    axes = axes.ravel()
    
    for i in range(4):
        path = random_walk_2d(1000)
        x_coords, y_coords = path
        
        axes[i].plot(x_coords, y_coords, marker='.')
        axes[i].scatter([x_coords[0]], [y_coords[0]], color='green', s=100, label='Start')
        axes[i].scatter([x_coords[-1]], [y_coords[-1]], color='red', s=100, label='End')
        axes[i].axis('equal')
        axes[i].legend()
        axes[i].set_title(f'Trajectory {i+1}')
    
    plt.tight_layout()
    # TODO: 实现多个轨迹的绘制
    # 提示：
    # 1. 创建2x2的子图布局
    # 2. 对每个子图重复以下步骤：
    #    - 生成随机行走轨迹
    #    - 绘制轨迹线
    #    - 标记起点和终点
    #    - 设置标题和图例
    pass

if __name__ == "__main__":
     plt.figure(figsize=(8, 8))
    path = random_walk_2d(1000)
    plot_single_walk(path)
    plt.title('Single Random Walk Trajectory')
    plt.show()
    
    # Task 2: Four different random walk trajectories
    plot_multiple_walks()
    plt.show()
# Task 2: Four different random walk trajectories
    plot_multiple_walks()
    plt.show()
    # TODO: 完成主程序逻辑
    # 1. 生成并绘制单个轨迹
    # 2. 生成并绘制多个轨迹
    pass
