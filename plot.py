import matplotlib.pyplot as plt
import numpy as np
import os
import math

eval_types = ['score', 'human_normalized_score', 'der_normalized_score', 'nature_normalized_score']

def average_over_several_runs(folder, eval_type):
    data_all = []
    min_length = np.inf
    runs = os.listdir(folder)
    for run in runs:
        data = np.loadtxt(folder+'/'+run+'/files/score.csv', delimiter=',', skiprows=1)
        eval_freq = data[1, 0] - data[0, 0]
        data_all.append(data[:, 1+eval_type])
        if data.shape[0] < min_length:
            min_length = data.shape[0]
    average = np.zeros([len(runs), min_length])
    for i in range(len(runs)):
        average[i, :] = data_all[i][:min_length]
    mean = np.mean(average, axis=0)
    std = np.std(average, axis=0)
    print(folder)
    print(mean[-1])
    return mean, std, eval_freq/1000

def plot_several_folders(prefix, folders=None, label_list=None, plot_or_save='save', title='', eval_type=0):
    plt.rcParams["figure.figsize"] = (10, 8)
    fig, axs = plt.subplots(1, 1)
    if folders is None:
        files = os.listdir('saved_exps/'+prefix)
        folders = label_list = sorted([i for i in files if not i.endswith('.png')], reverse=True)
        # print(folders)
    for i in range(len(folders)):
        folder_name = 'saved_exps/'+prefix+'/'+folders[i]
        num_runs = len(os.listdir(folder_name))
        mean_all, std_all, eval_freq = average_over_several_runs(folder_name, eval_type)
        
        axs_plot = axs
            
        # plot variance
        if label_list[i] == 'ours':
            axs_plot.fill_between(eval_freq*range(len(mean_all)),
                    mean_all - std_all/math.sqrt(num_runs),
                    mean_all + std_all/math.sqrt(num_runs), alpha=0.4, color='C3')
        else:
            axs_plot.fill_between(eval_freq*range(len(mean_all)),
                    mean_all - std_all/math.sqrt(num_runs),
                    mean_all + std_all/math.sqrt(num_runs), alpha=0.4)
        if len(label_list) == len(folders):
            # specify label
            if label_list[i] == 'ours':
                axs_plot.plot(eval_freq*range(len(mean_all)), mean_all, label=label_list[i], color='C3')
            else:
                axs_plot.plot(eval_freq * range(len(mean_all)), mean_all, label=label_list[i])
        else:
            axs_plot.plot(eval_freq*range(len(mean_all)), mean_all, label=folders[i])

        axs_plot.set_xlabel('evaluation steps(x1000)')
        axs_plot.set_ylabel(eval_types[eval_type])
        axs_plot.legend(fontsize=10)
        # axs_plot.set_title(eval_env_type[j])
        axs_plot.set_title(title)
    if plot_or_save == 'plot':
        plt.show()
    else:
        plt.savefig('saved_figs/'+title)

prefix = 'pong'
folders_1 = None
title = prefix
plot_several_folders(prefix, folders_1, label_list=folders_1, title=title, eval_type=0)

prefix = 'bank_heist'
folders_1 = None
title = prefix
plot_several_folders(prefix, folders_1, label_list=folders_1, title=title, eval_type=0)

prefix = 'breakout'
folders_1 = None
title = prefix
plot_several_folders(prefix, folders_1, label_list=folders_1, title=title, eval_type=0)

prefix = 'amidar'
folders_1 = None
title = prefix
plot_several_folders(prefix, folders_1, label_list=folders_1, title=title, eval_type=0)

prefix = 'ms_pacman'
folders_1 = None
title = prefix
plot_several_folders(prefix, folders_1, label_list=folders_1, title=title, eval_type=0)

prefix = 'boxing'
folders_1 = None
title = prefix
plot_several_folders(prefix, folders_1, label_list=folders_1, title=title, eval_type=0)

prefix = 'hero'
folders_1 = None
title = prefix
plot_several_folders(prefix, folders_1, label_list=folders_1, title=title, eval_type=0)

prefix = 'frostbite'
folders_1 = None
title = prefix
plot_several_folders(prefix, folders_1, label_list=folders_1, title=title, eval_type=0)

prefix = 'asterix'
folders_1 = None
title = prefix
plot_several_folders(prefix, folders_1, label_list=folders_1, title=title, eval_type=0)

prefix = 'battle_zone'
folders_1 = None
title = prefix
plot_several_folders(prefix, folders_1, label_list=folders_1, title=title, eval_type=0)

prefix = 'kangaroo'
folders_1 = None
title = prefix
plot_several_folders(prefix, folders_1, label_list=folders_1, title=title, eval_type=0)

prefix = 'road_runner'
folders_1 = None
title = prefix
plot_several_folders(prefix, folders_1, label_list=folders_1, title=title, eval_type=0)

prefix = 'up_n_down'
folders_1 = None
title = prefix
plot_several_folders(prefix, folders_1, label_list=folders_1, title=title, eval_type=0)