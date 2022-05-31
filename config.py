import numpy as np


class Config:
    # # HighD preprocessing
    # skip_frames = 10

    # field observation range
    obs_range_ahead = 50
    obs_range_behind = 20
    obs_range_left = 10
    obs_range_right = 10

    # Velocity field parameters
    GVF_size = (13, 17, 2)
    X_ = np.linspace(-(obs_range_behind - 10), obs_range_ahead - 5, obs_range_ahead - 5 + obs_range_behind - 10 + 1)
    Y_ = np.linspace(-obs_range_right, obs_range_left, obs_range_left + obs_range_right + 1)
    X_mesh, Y_mesh = np.meshgrid(X_, Y_)
    A = 1
    sigma_x = 15
    sigma_y = 1.5
    lambda_x = 0.4
    lambda_y = 0.9

    # Visualization
    car_width = 5
    car_height = 2
