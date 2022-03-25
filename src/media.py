# Imports
from tkinter import CENTER
from cairo import RasterSourcePattern
from pandas import read_csv, DataFrame
# from manim import *
from manim import *
# from manimlib.scene.graph_scene import GraphScene
from os import getcwd as _getcwd
from sys import path as _path

from torch import linspace

_path.insert(1, _getcwd())
# _path.insert(1, f"{_getcwdcls()}\\manim_scenes")

# from manim_scenes import *


# Constants
RAW_DATA_DIR = '../data/raw/'
PARAMS_FILE = 'input_params.csv'
DATA_FILE = 'output.csv'
DIVISOR = 60
SCALING = 30

# Loads a specific setup's output data
def load_setup_output(subsection: int, division: int = 0) -> DataFrame:
    data = read_csv(f"{RAW_DATA_DIR}data{division}_{subsection:02}/{DATA_FILE}")
    return data


class NumberLineTest(ThreeDScene):
    def construct(self):
        data = load_setup_output(0)
        data = data[["WorldPosition_X", "WorldPosition_Z", 'WorldPosition_Y']][data['acsys.CS.LapCount'] == 1]
        data['WorldPosition_Y'] = data['WorldPosition_Y']*5/SCALING
        data[['WorldPosition_X', 'WorldPosition_Z']] = data[['WorldPosition_X', 'WorldPosition_Z']]/SCALING
        self.coords = data.to_numpy()
        # self.coords = [[-4,6], [0,3], [1,2.5], [2,1], [2.5,-5]]
        self.length = len(self.coords)
        
        # self.set_camera_orientation(0,0)
        a = ThreeDAxes(x_range = [-60, 80, 20], y_range = [-90, 150, 20], axis_config={"include_ticks": True, "include_tip": False,})
        # a = Axes(x_range = [-10, 10, 1], y_range = [-10, 10, 1], x_length=3, y_length=20, axis_config={"include_ticks": False, "include_tip": False})
        f = ParametricFunction(self.func, t_range=[0, self.length-1, 1], color=BLUE, use_smoothing=False)
        # self.move_camera(2*PI/3, 2*PI/3, 10)
        # self.begin_ambient_camera_rotation(rate=0.2)

        tr = ValueTracker(0)

        # CHANGE DOT COLOUR FOR BREAKING AND ACCEL
        # T=tracker.get_value()
        # rgbcolor=[1,1-T,0+T]
        # m_color=rgb_to_color(rgbcolor)
        # upd_dot=Dot(color=m_color)
        # obj.become(upd_dot)

        dot = Dot(point=self.coords[0])
        dot.add_updater(lambda x: x.move_to(self.func(tr.get_value())))

        self.add(a, f, dot)
        self.set_camera_orientation(-PI/3,-PI/3)
        self.play(tr.animate.set_value(self.length), rate_func=rate_functions.linear, run_time=30)
        # self.play(MoveAlongPath(dot, f, rate_func=rate_functions.linear))
        self.wait()

    def func(self, t):
        t = int(t)
        self.f.set_color(PINK)
        if t < self.length:
            # return [t, t**2, 0]
            # print(self.coords[t])
            return (self.coords[t]).tolist()
        else:
            print(f'OVER! {t=}')
            return [t - (1 + t - self.length), 0, 0]


# class PlotMotion(Scene):
#     # CONFIG = {
#     #     "x_min": -60,
#     #     "x_max": 80,
#     #     "y_min": -90,
#     #     "y_max": 150,
#     #     "y_axis_config": {"tick_frequency": 10},
#     #     "y_labeled_nums": np.arange(0, 100, 10)
#     # }

#     def construct(self):
#         axes = Axes(x_range = [-60, 80], y_range=[-90, 150])

#         data = load_setup_output(0)
#         data = data[["WorldPosition_X", "WorldPosition_Z"]][data['acsys.CS.LapCount'] == 1]
#         self.coords = data.to_numpy()
#         self.data_size = len(self.coords)

#         self.hmm()

#         f = ParametricFunction(self.parametric_func, t_range=[DIVISOR, self.data_size, int(self.data_size/DIVISOR)])

#         self.add(axes, f)

#         self.add(axes)
    
#     def parametric_func(self, t):
#         # # TODO: instead of returning data points in succession, it will treat parameter with some units,
#         # #       and return data accordingly to that
#         # t = int(t)
#         # if t < self.data_size:
#         #     print(self.coords[t])
#         #     return list(self.coords[t])  # possibly need to add third dim, 0
#         # else:
#         #     print(f'mega hmmm at {t=}')
#         #     return [0,0]
#         return [t, 100*t**2]

    
#     def hmm(self):
#         count2 = 0
#         for i in self.coords:
#             if len(i) == 2:
#                 count2 += 1
#             else:
#                 print(i)
#         print(f'{count2=} {self.data_size=}')




# class PlotMotion(GraphScene):
#     CONFIG = {
#         "x_min": -60,
# 	    "x_max": 80,
# 	    "x_axis_width": 6,  # COULD I CHANGE TO 0?
# 	    "x_tick_frequency": 1,
# 	    "x_leftmost_tick": None, # Change if different from x_min
# 	    "x_labeled_nums": None,
# 	    "x_axis_label": "$x$",
# 	    "y_min": -90,  # MAYBE 80?
# 	    "y_max": 150,
# 	    "y_axis_height": 6,
# 	    "y_tick_frequency": 1,
# 	    "y_bottom_tick": None, # Change if different from y_min
# 	    "y_labeled_nums": None,
# 	    "y_axis_label": "$y$",
# 	    "axes_color": GREY,
# 	    "graph_origin": CENTER,
# 	    "exclude_zero_label": True,
# 	    # "num_graph_anchor_points": 25,
# 	    "default_graph_colors": [BLUE, GREEN, YELLOW],
# 	    "default_derivative_color": GREEN,
# 	    "default_input_color": YELLOW,
# 	    "default_riemann_start_color": BLUE,
# 	    "default_riemann_end_color": GREEN,
# 	    # "area_opacity": 0.8,
# 	    # "num_rects": 50
#     }
    
#     def construct(self):
#         self.setup_axes(animate=True)

#         data = load_setup_output(0)
#         coords = data[["WorldPosition_X", "WorldPosition_Z"]][data['acsys.CS.LapCount'] == 1].fillna(0).to_numpy().tolist()

#         data_points = VGroup(*[Dot(point=self.coords_to_point(coord['x'],coord['y']), radius=0.3) for coord in coords])
#         # self.play(Write(dots))
#         self.play(Write(data_points))


# class AnimateCarTrajectory(Scene):
#     def construct(self):
#         # self.setup_axes()
#         data = load_setup_output(0)
#         coords = data[["WorldPosition_X", "WorldPosition_Z"]][data['acsys.CS.LapCount'] == 1].to_numpy().tolist()
#         # dots = VGroup(*[Dot().move_to(self.coords_to_point(coord[0],coord[1])) for coord in coords])

#         self.add(dots)
