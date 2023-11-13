
import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from src import QuadTree, TkQuadTree

def test_sample():
    filename = "files/quadtree.txt"
    q = QuadTree.fromFile(filename)
    assert q.depth == 4

def test_single():
    filename = "files/quadtree_easy.txt"
    q = QuadTree.fromFile(filename)
    assert q.depth == 1

def test_file_right_num_elem():
    pass

def test_file_not_found():
    pass

def test_tkquadtree_sample():
    filename = "files/quadtree.txt"
    tkquadtree = TkQuadTree.fromFile(filename)
    assert tkquadtree.depth == 4

def test_tkquadtree_single():
    filename = "files/quadtree_easy.txt"
    tkquadtree = TkQuadTree.fromFile(filename)
    assert tkquadtree.depth == 1
