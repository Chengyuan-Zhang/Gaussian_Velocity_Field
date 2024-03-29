# Gaussian Velocity Field (GVF)

![Alt Text](Figs/GVF_highD_demo.gif)

### This repo provides a rudimentary implementation of Gaussian Velocity Field.
The Gaussian velocity field (GVF) in the paper "Spatiotemporal learning of multivehicle interaction patterns in lane-change scenarios" is a mathematical model used to represent the interactions between multiple vehicles during lane-change scenarios. The GVF is defined in a region of interest (ROI) around the ego vehicle (the vehicle of interest), which is a rectangular area symmetrically centered on the ego vehicle. The ROI is specified by three distances to the center of the ego vehicle: the front distance (d_front), the behind distance (d_behind), and the left/right distances (d_side).

The GVF is constructed over grid points in the ROI by meshing the width and length with intervals of 1 m and 5 m. A tensor with a size of 13 x 17 x 2 describes the GVF of each frame, where 2 represents the velocity components in the x and y directions.


## How to run

To look into the details of constructing GVF: check ```GVF.py```;

To visualize the result: ```python visualization.py```;

<center>
  <img src="./Figs/GVF_static_demo.png" width="85%" />
</center>

## Note

- The hyperparameters for Gaussian Velocity Field are manually defined in this repo. One can either set the
  hyperparameters manually according to the specific scenarios or learn from the data.
- GVF in this repo is constructed based on the relative velocity, one can easily base this model on the absolute
  velocity.

## Publications

- **Project website: [[web](https://chengyuan-zhang.github.io/Multivehicle-Interaction/)].**
- **Access our paper
  via: [[arXiv](https://arxiv.org/pdf/2003.00759v2.pdf)] or [[paper](https://ieeexplore.ieee.org/document/9357407)].**
- **Watch the demos
  via: [[YouTube](https://youtu.be/AcyDn43hb7I)] or [[Bilibili](https://www.bilibili.com/video/BV1BD4y1m7VL/)].**
- **Also check the supplements via: [[Spatiotemporal_Appendix.pdf](./files/Spatiotemporal_Appendix.pdf)].**

If you find the codes or paper useful for your research, please cite our paper:

```tex
@article{zhang2021spatiotemporal,
      title={Spatiotemporal learning of multivehicle interaction patterns in lane-change scenarios},
      author={Zhang, Chengyuan and Zhu, Jiacheng and Wang, Wenshuo and Xi, Junqiang},
      journal={IEEE Transactions on Intelligent Transportation Systems},
      year={2021},
      publisher={IEEE}
}

@inproceedings{zhang2019general,
  title={A general framework of learning multi-vehicle interaction patterns from video},
  author={Zhang, Chengyuan and Zhu, Jiacheng and Wang, Wenshuo and Zhao, Ding},
  booktitle={2019 IEEE Intelligent Transportation Systems Conference (ITSC)},
  pages={4323--4328},
  year={2019},
  organization={IEEE}
}

@inproceedings{wang2020learning,
  title={Learning Representations for Multi-Vehicle Spatiotemporal Interactions with Semi-Stochastic Potential Fields},
  author={Wang, Wenshuo and Zhang, Chengyuan and Wang, Pin and Chan, Ching-Yao},
  booktitle={2020 IEEE Intelligent Vehicles Symposium (IV)},
  pages={1935--1940},
  year={2020},
  organization={IEEE}
}
```

## Contact

**If you have any questions please feel free to contact
us:  [Chengyuan Zhang](https://chengyuanzhang.wixsite.com/home) (<enzozcy@gmail.com>)
and [Wenshuo Wang](http://wenshuow.com/) (<wwsbit@gmail.com>).**

## Future updates

We will provide more demos to construct GVF on the highD dataset soon.