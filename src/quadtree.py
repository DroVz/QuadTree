from __future__ import annotations
import pygame
class QuadTree:
    NB_NODES : int = 4
    def __init__(self, hg: bool | QuadTree, hd: bool | QuadTree, bd: bool | QuadTree,bg: bool | QuadTree):
        """
        TODO : com
        :param hg: 
        :param hd:
        :param bd:
        :param bg:
        """
        self.hg = hg
        self.hd = hd
        self.bd = bd
        self.bg = bg

    @property
    def depth(self) -> int:
        """
        Recursion depth of the quadtree
        :return: Depth of the quadtree
        """
        ROOT_DEPTH = 1
        return self.__find_deepest_depth(ROOT_DEPTH)

    def __find_deepest_depth(self, root_depth : int) :
        """
        :param root_depth:  Depth of the root
        :return: The deepest depth of the quadtree
        """
        quadtree_property_list = [self.hg, self.hd, self.bd, self.bg]
        list_of_depth_by_branch = []

        for quadtree_property in quadtree_property_list:
            if isinstance(quadtree_property, QuadTree):
                list_of_depth_by_branch.append(quadtree_property.__find_deepest_depth(root_depth + 1))
            else:
                list_of_depth_by_branch.append(root_depth)

        return max(list_of_depth_by_branch)

    @staticmethod
    def fromFile(filename: str) -> QuadTree:
        """
        Open a given file, containing a textual representation of a list
        :param filename: path of file to convert
        :return: Quadtree make by a file
        """
        representation_list_of_quadtree = eval(open(filename, "r", encoding='utf-8').read())
        return QuadTree.fromList(representation_list_of_quadtree)

    @staticmethod
    def fromList(data: list) -> QuadTree:
        """
        Generates a Quadtree from a list representation
        :param data: representation list of Quadtree
        :return: Quadtree make by a list
        """
        quadtree_branch = []

        if len(data) == QuadTree.NB_NODES :
            for element in data:
                if isinstance(element, list):
                    quadtree_branch.append(QuadTree.fromList(element))
                else:
                    quadtree_branch.append(element)
        else :
            raise Exception("the list does not contain the right number of elements")

        return QuadTree(quadtree_branch[0], quadtree_branch[1], quadtree_branch[2], quadtree_branch[3])

class TkQuadTree(QuadTree):
    X_POSITION = 0
    Y_POSITION = 0
    WIDTH_OF_SQUARE = 700

    def paint(self, screen):
        """
        TK representation of a Quadtree
        :param screen: drawing screen
        """
        pygame.draw.rect(screen,"red", [self.X_POSITION, self.Y_POSITION, self.WIDTH_OF_SQUARE, self.WIDTH_OF_SQUARE], 2)
        self.paint_square(screen, [self.X_POSITION, self.Y_POSITION], self.WIDTH_OF_SQUARE)


    def paint_square(self, screen, position : list, actual_width):
        """
        Draw a representation of quadtree
        :param screen: drawing screen
        :param position: position to start to draw
        :param actual_width: width of the quadtree representation
        """
        tkquadtree_property_list = [self.hg, self.hd, self.bd, self.bg]
        width_of_square = int(actual_width/2)
        index_to_select_corner = 0
        #TODO : make iterator class
        corner_position_list = [position, [position[0] + width_of_square, position[1]],
                                [position[0] + width_of_square, position[1] + width_of_square],
                                [position[0], position[1] + width_of_square]]

        for tkquadtree_property in tkquadtree_property_list :
            if isinstance(tkquadtree_property, TkQuadTree) :
                pygame.draw.rect(screen, "black",
                                 [corner_position_list[index_to_select_corner][0], corner_position_list[index_to_select_corner][1], width_of_square,
                                  width_of_square], 2)
                tkquadtree_property.paint_square(screen, corner_position_list[index_to_select_corner], width_of_square)
            elif isinstance(tkquadtree_property, int) :
                if tkquadtree_property :
                    pygame.draw.rect(screen, "black",
                                     [int(corner_position_list[index_to_select_corner][0]), int(corner_position_list[index_to_select_corner][1]), width_of_square,
                                      width_of_square], width_of_square)
                else :
                    pygame.draw.rect(screen, "black",
                                     [int(corner_position_list[index_to_select_corner][0]), int(corner_position_list[index_to_select_corner][1]), width_of_square,
                                      width_of_square], 2)
            index_to_select_corner += 1

    @staticmethod
    def fromFile(filename: str) -> TkQuadTree:
        """
        Open a given file, containing a textual representation of a list
        :param filename: path of file to convert
        :return: TkQuadTree make by a file
        """
        file_content = open(filename,"r")
        representation_list_of_quadTree = eval(file_content.read())
        return TkQuadTree.fromList(representation_list_of_quadTree)

    @staticmethod
    def fromList(data: list) -> TkQuadTree:
        """
        Generates a TkQuadTree from a list representation
        :param data: representation list of TkQuadTree
        :return: TkQuadTree make by a list
        """
        tkquadtree_branch = []

        if len(data) == TkQuadTree.NB_NODES:
            for element in data:
                if isinstance(element, list):
                    tkquadtree_branch.append(TkQuadTree.fromList(element))
                else:
                    tkquadtree_branch.append(element)
        else:
            raise Exception("the list does not contain the right number of elements")

        return TkQuadTree(tkquadtree_branch[0], tkquadtree_branch[1], tkquadtree_branch[2], tkquadtree_branch[3])
