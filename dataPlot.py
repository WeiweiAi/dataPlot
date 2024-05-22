import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

def subplots_ajdust(fig_cfg, **subtitle_kwargs):
    """Create a figure and a set of subplots with the specified configuration.
    
    Parameters
    ----------
    fig_cfg : dict
        A dictionary containing the configuration of the figure and subplots.
        The dictionary should contain the following keys:
        - num_rows: int, default=1
            Number of rows of subplots.
        - num_cols: int, default=1
            Number of columns of subplots.
        - width: float, default=6
            Width of the figure in inches, usually between 2.63 and 7.5.
        - height: float, default=6
            Height of the figure in inches, maximum 8.75
        - fig_title: str, default=None
            Title of the figure.
        - title_y: float, default=0.98
            The y location of the text in figure coordinates.
        - fontsize: int, default=10
            Setting font_size in matplotlib.
        - left: float, default=0.125
            The left side of the subplots of the figure, as a fraction of the figure width.
        - right: float, default=0.9
            The right side of the subplots of the figure, as a fraction of the figure width.
        - bottom: float, default=0.1
            The bottom of the subplots of the figure, as a fraction of the figure width.
        - top: float, default=0.9
            The top of the subplots of the figure, as a fraction of the figure width.
        - wspace: float, default=0.2
            The amount of width reserved for space between subplots, expressed as a fraction of the average axis width.
        - hspace: float, default=0.2
            The amount of height reserved for space between subplots, expressed as a fraction of the average axis height.
        - legend_kwargs: dict
            https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.legend.html
        - subtitle_kwargs : dict
            Additional keyword arguments for the suptitle function.
            https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.suptitle.html

    Returns
    -------
    fig : matplotlib.figure.Figure
        The figure object.
    axs : an array of Axes objects
        The array of axes objects.

    """   
    left = fig_cfg.get('left', 0.125)  
    right = fig_cfg.get('right', 0.9)  
    bottom = fig_cfg.get('bottom', 0.05) 
    top = fig_cfg.get('top', 0.9)     
    wspace = fig_cfg.get('wspace', 0.2)     
    hspace = fig_cfg.get('hspace', 0.2)    
    rows, cols = fig_cfg.get('num_rows', 1), fig_cfg.get('num_cols', 1)
    width, height = fig_cfg.get('width', 6), fig_cfg.get('height', 9)    
    plt.rcParams['font.size'] = fig_cfg.get('fontsize', 10)
    fig, axs = plt.subplots(rows,cols,figsize=(width, height),squeeze=False)
    fig.suptitle(fig_cfg.get('fig_title', ''), y=fig_cfg.get('title_y', 0.98),  **fig_cfg.get('subtitle_kwargs', {}))
    fig.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)

    return fig, axs

def plot_line2D(fig_cfg, plot_cfg, line_cfg):
    """Plot the data on the specified axes as lines.

    Parameters
    ----------
    axs : an array of Axes objects
        The array of axes objects.
    plot_cfg : dict
        A dictionary containing the configuration of the plots
        {'plot_id': dict, ...}
        The dictionary may contain the following keys:
        - xlabel: str
            Label of the x-axis.
        - ylabel: str
            Label of the y-axis.
        - xlim: tuple
            Tuple containing the lower and upper limits of the x-axis.
        - ylim: tuple
            Tuple containing the lower and upper limits of the y-axis.
        - xscale: str, default='linear'
            Scale of the x-axis.
        - yscale: str, default='linear'
            Scale of the y-axis.
        - xticks: 1D array-like
            List of ticks for the x-axis.
        - xticks_percentage: bool, default=False
            If True, the x-axis will be formatted as a percentage.
        - yticks: 1D array-like
            List of ticks for the y-axis.
        - yticks_percentage: bool, default=False
            If True, the y-axis will be formatted as a percentage.
        - xticks_kwargs: dict, default={}
            Additional properties for the xticks.
            https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html
        - yticks_kwargs: dict, default={}
            Additional properties for the yticks.
            https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html
        - show_grid: 'major', 'minor', 'both'
            The grid lines to apply the changes on.
        - grid_axis: 'both', 'x', 'y', default='both'
            Axis on which the grid will be shown. Only applicable if show_grid is present.
        - grid_properties: dict, default={}
            Additional properties for the grid.
            https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grid.html
            Only applicable if show_grid is present.
        - line: list, default=[]
            List of line ids to be plotted.
        - legend: list, default=[]
            List of line ids to be included in the legend.
        - legends_position: str, default='best'
            Position of the legend.
            https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html
        - lgdncol: int, default=1
            Number of columns in the legend.
        - bbox_to_anchor: tuple, default=None
            The bbox that the legend will be anchored.
            2-tuple (x, y), or 4-tuple of floats (x, y, width, height).
        - title: str, default=None
            Title of the plot.
        - title_y: float, default=1.0
            The y location of the text in figure coordinates.

    line_cfg : dict
        A dictionary containing the configuration of the lines
        {'line_id': dict, ...}
        The dictionary may contain the following keys:
        - xdata: tuple, mandatory
            Tuple containing the file name and the column name of the x-axis data.
        - ydata: tuple, mandatory
            Tuple containing the file name and the column name of the y-axis data.
        - rightYAxis: str, default=False
            Label of the right y-axis.
        - ylim_right: tuple, default=False
            Tuple containing the lower and upper limits of the right y-axis.
        _ rightYAxis_percentage: bool, default=False
            If True, the right y-axis will be formatted as a percentage.
        - color: str, default='b'
            Color of the line, such as 'b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'.
        - linestyle: str, default='-'
            Style of the line, such as '-', '--', '-.', ':'.
        - marker: str, default=None
            Style of the marker.
            https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html
        - markevery: int, default=1
            Plot only every nth marker.
        - label: str, default=None
            Label of the line in the legend.
        - line_kwargs: dict, default={}
            Additional properties for the line.
            https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html

    save_fig : dict
        A dictionary containing the configuration of saving the figure.
        The dictionary may contain the following keys:
        - fig_format: str, default='png'
            Format of the saved figure, such as 'png', 'pdf', 'svg', 'eps'.
        - file_path: str, default='./'
            Path of the saved figure.
        - filename: str, default='new_fig'
            Name of the saved figure.

    """
    fig, axs=subplots_ajdust(fig_cfg)
    # Read data from the files first to avoid reading the same file multiple times
    # If the same file is used for multiple lines, read the file once and use the data for all the lines
    data_files = {}
    data_file_names = {}
    nfiles = 0
    for line_id, line_data in line_cfg.items():
        if 'xdata' in line_data:
            if  line_data['xdata'][0] not in data_file_names:
                # add the file to the data_files dictionary
                nfiles += 1
                data_files[nfiles] = pd.read_csv(line_data['xdata'][0])
                data_file_names[nfiles] = line_data['xdata'][0]
                line_data['xdata_array'] = data_files[nfiles][line_data['xdata'][1]]
            else:
                # find the file in the data_files dictionary and use the data
                for k, v in data_file_names.items():
                    if v == line_data['xdata'][0]:
                        line_data['xdata_array'] = data_files[k][line_data['xdata'][1]]
                        break
        elif 'xdata_array' in line_data:
            pass
        else:
            raise ValueError('xdata or xdata_array is missing in line_cfg')
            
        if 'ydata' in line_data:
            if line_data['ydata'][0] not in data_file_names:
                # add the file to the data_files dictionary
                nfiles += 1
                data_file_names[nfiles] = line_data['ydata'][0]
                data_files[nfiles] = pd.read_csv(line_data['ydata'][0])
                line_data['ydata_array'] = data_files[nfiles][line_data['ydata'][1]]
            else:
                # find the file in the data_files dictionary and use the data
                for k, v in data_file_names.items():
                    if v == line_data['ydata'][0]:
                        line_data['ydata_array'] = data_files[k][line_data['ydata'][1]]
                        break
        elif 'ydata_array' in line_data:
            pass
        else:
            raise ValueError('ydata or ydata_array is missing in line_cfg')

    for plot_id, plot_data in plot_cfg.items():
        ax = axs.flatten()[plot_id-1]
        if 'xlabel' in plot_data :
            ax.set_xlabel(plot_data['xlabel'])
        if 'ylabel' in plot_data :
            ax.set_ylabel(plot_data['ylabel'])
        if 'xlim' in plot_data:
            ax.set_xlim(plot_data['xlim'])
        if 'ylim' in plot_data:
            ax.set_ylim(plot_data['ylim'])
        ax.set_xscale(plot_data.get('xscale', 'linear'))
        ax.set_yscale(plot_data.get('yscale', 'linear'))
        if plot_data.get('xticks', None):
            ax.set_xticks(plot_data['xticks'],**plot_data.get('xticks_kwargs', {}))
        if plot_data.get('yticks', None):
            ax.set_yticks(plot_data['yticks'],**plot_data.get('yticks_kwargs', {}))
        if plot_data.get('xticks_percentage', False):
            ax.xaxis.set_major_formatter(PercentFormatter())
        if plot_data.get('yticks_percentage', False):
            ax.yaxis.set_major_formatter(PercentFormatter())
        if 'title' in plot_data:
            ax.set_title(plot_data['title'],y=plot_data.get('title_y', 1.0))                    
        if plot_data.get('show_grid', False):
            ax.grid(visible=True, which=plot_data['show_grid'], axis=plot_data.get('grid_axis', 'both'), **plot_data.get('grid_properties', {}))
        handles = {}
        for i, line_id in enumerate(plot_data.get('line', [])):
            xdata = line_cfg[line_id]['xdata_array']
            ydata = line_cfg[line_id]['ydata_array']    
            if line_cfg[line_id].get('rightYAxis', False):
                ax2 = ax.twinx()
                ax2.set_ylabel(line_cfg[line_id]['rightYAxis'])
                if line_cfg[line_id].get('ylim_right', False):
                    ax2.set_ylim(line_cfg[line_id]['ylim_right'])
                if line_cfg[line_id].get('rightYAxis_percentage', False):
                    ax2.yaxis.set_major_formatter(PercentFormatter())
                handles[line_id],=ax2.plot(xdata, ydata, color=line_cfg[line_id].get('color', 'b'), linestyle=line_cfg[line_id].get('linestyle', '-'),
                    marker=line_cfg[line_id].get('marker'), markevery=line_cfg[line_id].get('markevery', 1),
                    label=line_cfg[line_id].get('label'), **line_cfg[line_id].get('line_kwargs', {}))
            else:
                handles[line_id],=ax.plot(xdata, ydata, color=line_cfg[line_id].get('color', 'b'), linestyle=line_cfg[line_id].get('linestyle', '-'),
                    marker=line_cfg[line_id].get('marker'), markevery=line_cfg[line_id].get('markevery', 1),
                    label=line_cfg[line_id].get('label'), **line_cfg[line_id].get('line_kwargs', {}))
        [ymin,ymax] =ax.get_ylim() 
        if 'xspan' in plot_data and 'yspan' in plot_data: 
           ax.fill_between(plot_data['xspan'], ymin, ymax, where=plot_data['yspan'] > 0, **plot_data.get('fill_properties', {}))
        ax.set_ylim([ymin,ymax])
        # Only show the legend specified in the plot_cfg
        if 'legend' in plot_data:
            handles_list = [handles[i] for i in plot_data['legend']]
            ax.legend(handles=handles_list,loc=plot_data.get('legends_position', 'best'), ncol=plot_data.get('lgdncol', 1))
            if 'bbox_to_anchor' in plot_data:
                ax.legend( bbox_to_anchor=plot_data.get('bbox_to_anchor'))
    if fig_cfg.get('legend_id', False):
        # Collect lines and labels for figure legend
        lines_labels = [axs.flatten()[legend_id-1].get_legend_handles_labels() for legend_id in fig_cfg['legend_id']]
        lines, labels = [sum(lol, []) for lol in zip(*lines_labels)]
        # Create figure legend
        fig.legend(lines, labels, **fig_cfg.get('legend_kwargs', {}))

    full_path = fig_cfg.get('file_path', './') + fig_cfg.get('filename', 'new_fig') + '.' + fig_cfg.get('fig_format', 'png')
    plt.savefig(full_path)
    if fig_cfg.get('fig_format', 'png') != 'png':
            full_path_png = fig_cfg.get('file_path', './') + fig_cfg.get('filename', 'new_fig') + '.png'
            plt.savefig(full_path_png)
    plt.show()

if __name__ == '__main__':

    data_path='./data/'
    save_fig = {'fig_format': 'png', 'file_path': data_path, 'filename': 'BG_fit_fig10'}
    filename_50 = data_path+'Fig10_Parent1992_50mV.csv'
    filename_150 = data_path+'Fig10_Parent1992_150mV.csv'
    filename_BG_150 = data_path+'report_task_SGLT1_BG_step_fig10_150mV_post.csv'
    filename_BG_50 = data_path+'report_task_SGLT1_BG_step_fig10_50mV_post.csv'
    filename_50_sugar = data_path+'Fig10_Parent1992_50mV_sugar.csv'
    filename_150_sugar = data_path+'Fig10_Parent1992_150mV_sugar.csv'
    filename_BG_150_sugar = data_path+'report_task_SGLT1_BG_step_fig10_150mV_sugar_post.csv'
    filename_BG_50_sugar = data_path+'report_task_SGLT1_BG_step_fig10_50mV_sugar_post.csv'


    fig_cfg = {'num_rows': 1, 'num_cols': 2, 'width':8, 'height':4, 'fig_title': None, 'title_y': 0.98, 'fontsize': 8, 
               'left': 0.1, 'bottom': 0.25, 'right': 0.95, 'top': 0.95, 'wspace': 0.25, 'hspace': 0.2}
    
    plot_cfg = {}
    line_cfg = {}

    line_cfg[1] = { 'xdata': (filename_50,'x'), 'ydata':(filename_50,'Curve1'),
                    'color': 'k', 'linestyle': '-',  'label': 'Parent et al. (1992a) @50mV'}
    line_cfg[2] = { 'xdata': (filename_150,'x'), 'ydata':(filename_150,'Curve1'),
                    'color': 'k', 'linestyle': '-.',  'label': 'Parent et al. (1992a) @-150mV'}
    line_cfg[3] = { 'xdata': (filename_BG_50,'tms'), 'ydata':(filename_BG_50,'Ii'),
                    'color': 'b', 'linestyle': '--',  'label': 'Bond graph @50mV'}
    line_cfg[4] = { 'xdata': (filename_BG_150,'tms'), 'ydata':(filename_BG_150,'Ii'),
                    'color': 'r', 'linestyle': '--',  'label': 'Bond graph @-150mV'}
    line_cfg[5] = { 'xdata': (filename_50_sugar,'x'), 'ydata':(filename_50_sugar,'Curve1'),
                    'color': 'k', 'linestyle': '-',  'label': 'Parent et al. (1992a) @50mV'}
    line_cfg[6] = { 'xdata': (filename_150_sugar,'x'), 'ydata':(filename_150_sugar,'Curve1'),
                    'color': 'k', 'linestyle': '-.',  'label': 'Parent et al. (1992a) @-150mV'}
    line_cfg[7] = { 'xdata': (filename_BG_50_sugar,'tms'), 'ydata':(filename_BG_50_sugar,'Ii'),
                    'color': 'b', 'linestyle': '--',  'label': 'Bond graph @50mV'}
    line_cfg[8] = { 'xdata': (filename_BG_150_sugar,'tms'), 'ydata':(filename_BG_150_sugar,'Ii'),
                    'color': 'r', 'linestyle': '--',  'label': 'Bond graph @-150mV' }
    line_cfg[9] = { 'xdata': (filename_BG_150_sugar,'tms'), 'ydata':(filename_BG_150_sugar,'Ii'),
                    'color': 'm', 'linestyle': '--',  'label': 'Bond graph @-150mV', 'rightYAxis': '%', 'rightYAxis_percentage': True, 'ylim_right': [-200, 100]}

    plot_cfg[1] = {'ylabel': 'i (nA)', 'xlabel': 'Time (ms)','show_grid': 'both', 'grid_axis': 'both',  'ylim': [-500, 1500], 'xlim': [0, 80],
                    'line': [1,2,3,4], 'legend': [1,2,3,4], 'title': '(a) Before the addition of sugar','title_y': -0.25}
    plot_cfg[2] = {'ylabel': 'i (nA)', 'xlabel': 'Time (ms)','show_grid': 'both', 'grid_axis': 'both',  'ylim': [-500, 400], 'xlim': [0, 80],
                    'line': [5,6,7,8,9], 'legend': [5,6,7,8,9], 'title': '(b) After the addition of sugar','title_y': -0.25}

    plot_line2D(fig_cfg, plot_cfg, line_cfg)