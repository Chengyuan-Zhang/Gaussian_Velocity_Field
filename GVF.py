import numpy as np
from config import Config
from numpy.linalg import inv
from sklearn.metrics.pairwise import rbf_kernel


def RBF_kernel(XA, XB, length_scale=[15, 1.5], A=1):
    # In our paper, we set A=1, length_scale_x=15, length_scale_y=1.5.
    # Note that these parameters can be either learned from data or
    # manually set according to the specific scenarios.
    length_scale_x = length_scale[0]
    length_scale_y = length_scale[1]
    X_dist = A * rbf_kernel(XA[:, [0]], XB[:, [0]], gamma=0.5 / length_scale_x ** 2)
    Y_dist = A * rbf_kernel(XA[:, [1]], XB[:, [1]], gamma=0.5 / length_scale_y ** 2)
    return X_dist * Y_dist


def posterior(X, Xtest, y, length_scale=[15, 1.5]):
    # compute the mean at our test points.
    N, n = len(X), len(Xtest)
    K = RBF_kernel(X, X, length_scale)
    K_ = RBF_kernel(Xtest, Xtest, length_scale)
    KK = RBF_kernel(Xtest, X, length_scale)
    Mu = KK @ inv(K) @ y
    Sigma = K_ - KK @ inv(K) @ KK.T
    return Mu, Sigma


def construct_GVF(P, Ptest, V, length_scale=[15, 1.5]):
    # The notations follow those defined in our paper, where P = [X, Y] and V = [VX, VY] represents
    # the relative positions and velocities of other vehicles to the ego vehicle, accordingly;
    # Ptest represents the test point positions that we want to evaluate to construct GVF;

    VXX, _ = posterior(P, Ptest, V[:, 0], length_scale)
    VYY, _ = posterior(P, Ptest, V[:, 1], length_scale)
    return VXX, VYY


def construct_GVF_for_highD(others_info, ego_info):
    x_e = ego_info['bbox'][0] + 0.5 * ego_info['bbox'][2]
    y_e = ego_info['bbox'][1] + 0.5 * ego_info['bbox'][3]
    vx_e = ego_info['xVelocity']
    vy_e = ego_info['yVelocity']
    ax_e = ego_info['xAcceleration']
    ay_e = ego_info['yAcceleration']
    P_o = []
    V_o_to_e = []
    A_o = []
    VXX = np.zeros_like(Config.X_mesh)
    VYY = np.zeros_like(Config.Y_mesh)
    for i in range(len(others_info)):
        if not others_info[i] or others_info[i]['id'] == ego_info['id']:  # others_info still includes ego_info
            continue
        else:
            x_o = others_info[i]['bbox'][0] + 0.5 * others_info[i]['bbox'][2]
            y_o = others_info[i]['bbox'][1] + 0.5 * others_info[i]['bbox'][3]
            if (x_o < x_e + Config.obs_range_ahead) & (x_o > x_e - Config.obs_range_behind) & (
                    y_o < y_e + Config.obs_range_left) & (y_o > y_e - Config.obs_range_right):
                P_o.append([x_o, y_o])
                V_o_to_e.append([others_info[i]['xVelocity'] - vx_e, others_info[i]['yVelocity'] - vy_e])
                A_o.append([others_info[i]['xAcceleration'], others_info[i]['yAcceleration']])
    P_test = np.array([Config.X_mesh.reshape(-1), Config.Y_mesh.reshape(-1)]).T
    if P_o:
        VXX, VYY = construct_GVF(np.array(P_o), P_test, np.array(V_o_to_e),
                                 length_scale=[Config.sigma_x, Config.sigma_y])
        pass
    return VXX.reshape(Config.X_mesh.shape), VYY.reshape(Config.Y_mesh.shape)
