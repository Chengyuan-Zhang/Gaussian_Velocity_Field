import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.patches as mpatches
from GVF import construct_GVF_for_highD
from config import Config


def GVF_static_demo():
    plt.rcParams["font.family"] = "Times New Roman"
    matplotlib.rcParams['font.size'] = 12
    matplotlib.rcParams['font.family'] = 'Times New Roman'

    # Try to play with these parameters to see how each may change the velocity field
    vx_ego = 20
    vy_ego = 0

    vx_other0 = 30
    vy_other0 = -6
    x_other0 = 25
    y_other0 = 4

    vx_other1 = 10
    vy_other1 = 3
    x_other1 = 15
    y_other1 = -4

    ego_info = {'id': 0,
                'frame': 0,
                'bbox': np.transpose(np.array(
                    [0 - 0.5 * Config.car_width, 0 - 0.5 * Config.car_height,
                     Config.car_width, Config.car_height])),
                'xVelocity': vx_ego,
                'yVelocity': vy_ego,
                'xAcceleration': 0.5,
                'yAcceleration': 0
                }
    others_info = [None] * 2
    others_info[0] = {'id': 1,
                      'frame': 0,
                      'bbox': np.transpose(np.array([x_other0 - 0.5 * Config.car_width,
                                                     y_other0 - 0.5 * Config.car_height,
                                                     Config.car_width, Config.car_height])),
                      'xVelocity': vx_other0,
                      'yVelocity': vy_other0,
                      'xAcceleration': 1,
                      'yAcceleration': 0
                      }
    others_info[1] = {'id': 2,
                      'frame': 0,
                      'bbox': np.transpose(np.array([x_other1 - 0.5 * Config.car_width,
                                                     y_other1 - 0.5 * Config.car_height,
                                                     Config.car_width, Config.car_height])),
                      'xVelocity': vx_other1,
                      'yVelocity': vy_other1,
                      'xAcceleration': 1,
                      'yAcceleration': 0
                      }

    GVF_x, GVF_y = construct_GVF_for_highD(others_info, ego_info)
    X_mesh, Y_mesh = np.meshgrid(Config.X_ + 0, Config.Y_ + 0)
    x_e = 0
    y_e = 0

    line_w = 3
    grey_scale = 1.0
    color = (grey_scale, grey_scale, grey_scale)

    fig = plt.figure(figsize=(8, 4))
    ##############################
    ax = plt.subplot(1, 1, 1)

    cmap0 = 'jet'
    GVF_all = np.sqrt(GVF_x ** 2 + GVF_y ** 2)
    plt.pcolormesh(X_mesh, Y_mesh, GVF_all, cmap=cmap0, shading='gouraud')
    ax.quiver(X_mesh, Y_mesh, GVF_x, GVF_y, scale=300)

    ax = plt.gca()
    ax.add_patch(
        mpatches.Rectangle((ego_info['bbox'][0], ego_info['bbox'][1]), ego_info['bbox'][2] + .5, ego_info['bbox'][3],
                           edgecolor='black', facecolor="red"))
    for i in range(len(others_info)):
        if not others_info[i] or others_info[i]['id'] == ego_info['id']:  # others_info still includes ego_info
            continue
        else:
            if Config.X_[0] + x_e < others_info[i]['bbox'][0] + 0.5 * others_info[i]['bbox'][2] < Config.X_[
                -1] + x_e and \
                    Config.Y_[0] + y_e < others_info[i]['bbox'][1] + 0.5 * others_info[i]['bbox'][3] < Config.Y_[
                -1] + y_e:
                ax.add_patch(
                    mpatches.Rectangle((others_info[i]['bbox'][0], others_info[i]['bbox'][1]),
                                       others_info[i]['bbox'][2], others_info[i]['bbox'][3],
                                       edgecolor='black', facecolor="grey"))

    ax.text(x_e - 2.5, y_e - 0.5, '$20$ m/s',
            color=color, fontsize=16)
    ax.annotate('', xy=(x_other0, y_other0),
                xytext=(x_other0 + 5, y_other0 - 3),
                arrowprops=dict(arrowstyle="<-",
                                color=color,
                                linewidth=3,
                                mutation_scale=30))
    ax.text(x_other0 + 5.5, y_other0 - 3, '$30$ m/s',
            color=color, fontsize=16, bbox=dict(facecolor='k', alpha=0.3))
    ax.annotate('', xy=(x_other1, y_other1),
                xytext=(x_other1 - 5, y_other1 + 1),
                arrowprops=dict(arrowstyle="<-",
                                color=color,
                                linewidth=3,
                                mutation_scale=30))
    ax.text(x_other1 - 6, y_other1 + 2, '$10$ m/s',
            color=color, fontsize=16, bbox=dict(facecolor='k', alpha=0.3))
    plt.plot([-Config.obs_range_behind + 10, Config.obs_range_ahead - 5], [2, 2], "--w", linewidth=line_w)
    plt.plot([-Config.obs_range_behind + 10, Config.obs_range_ahead - 5], [-2, -2], "--w", linewidth=line_w)
    plt.plot([-Config.obs_range_behind + 10, Config.obs_range_ahead - 5], [6, 6], "-w", linewidth=line_w)
    plt.plot([-Config.obs_range_behind + 10, Config.obs_range_ahead - 5], [-6, -6], "-w", linewidth=line_w)
    plt.ylabel('$y$ [m]', fontsize=12)
    plt.xlabel('$x$ [m]', fontsize=12)
    plt.title('Gaussian Velocity Field')
    # plt.grid(linestyle=':')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    GVF_static_demo()
