## graph ##
## by JARJARBIN'S STUDIO ##
## v1.2 ##

from typing import Any, Generator

class GUI:
    """
        GUI for Graph
    """

    import numpy as np
    import matplotlib.pyplot as plt

    def show(self: object, r: int | float = 10) -> None:

        """
            show Graph as a circle in a pyplot window

            Parameter :
                - self (object) : Graph object
                - r (int | float) = 10 : radius of the circle
        """

        dots = {}
        n = 0
        nodes_name = []
        for node in self.nodes:
            nodes_name.append(node)
        for t in self.get_nodes_pos():
            x, y = r * GUI.np.cos(t), r * GUI.np.sin(t)
            if self.nodes[nodes_name[n]].pos == (None, None):
                dots[nodes_name[n]] = (x, y)
            else:
                dots[nodes_name[n]] = self.nodes[nodes_name[n]].pos
            n += 1
        for dot in dots:
            x, y = dots[dot]
            x_signe = 1
            if x < 0:
                x_signe = -3.5
            y_signe = 1
            if y < 0:
                y_signe = -3.5
            links_xy = []
            for link in self.nodes[dot].links:
                links_xy.append(dots[link.name])
            GUI.plt.plot(x, y, 'bo')
            GUI.plt.text(x + (x_signe * 0.2), y + (y_signe * 0.2), self.nodes[dot].name)
            for link in links_xy:
                link_x, link_y = link
                dist_x = 0.90 * (link_x - x)
                dist_y = 0.90 * (link_y - y)
                GUI.plt.arrow(x, y, dist_x, dist_y, width=0.05, head_width=0.5)
        GUI.plt.title("Graph viewer")
        GUI.plt.show()

    def get_nodes_pos(self: object) -> Generator[int | float | Any, Any, None]:

        """
            get x and y position of all nodes

            Parameter :
                - self (object) : Graph object

            Return :
                dict : positions
        """

        for j in range(self.get_size()):
            yield j * (2 * GUI.np.pi / self.get_size())