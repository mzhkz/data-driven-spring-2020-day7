import matplotlib.pyplot as plt

names = ["{}".format(x) for x in range(1, 11)]

def describe(pairs):
    global names
    fig = plt.figure()
    ax = fig.add_subplot(111)

    table_vals = [['-' for i in range(0, 10)] for i in range(0, 10)]

    for p in pairs:
        table_vals[n_people(p[0])][n_people(p[1])] = p[2]
        table_vals[n_people(p[1])][n_people(p[0])] = p[2]
    
    col_labels = names
    row_labels = names

    # Draw table
    the_table = plt.table(cellText=table_vals,colWidths=[0.1] * 10,rowLabels=row_labels,colLabels=col_labels,loc='center')
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(11)
    the_table.scale(1, 1)
    # Removing ticks and spines enables you to get the figure only with table
    plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
    plt.tick_params(axis='y', which='both', right=False, left=False, labelleft=False)
    for pos in ['right','top','bottom','left']:
        plt.gca().spines[pos].set_visible(False)
    plt.show()

def n_people(p):
   return int(p.name[2:4]) -1

