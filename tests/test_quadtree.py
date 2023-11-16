from src import QuadTreeElementException
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
    try:
        filename = "files/quadtree_element_error.txt"
        q = QuadTree.fromFile(filename)
    except QuadTreeElementException:
        assert True

def test_file_not_found():
    try:
        filename = "files/quadtree_not_found.txt"
        q = QuadTree.fromFile(filename)
    except FileNotFoundError:
        assert True

def test_tkquadtree_sample():
    filename = "files/quadtree.txt"
    tkquadtree = TkQuadTree.fromFile(filename)
    assert tkquadtree.depth == 4

def test_tkquadtree_single():
    filename = "files/quadtree_easy.txt"
    tkquadtree = TkQuadTree.fromFile(filename)
    assert tkquadtree.depth == 1

def test_tkquadtree_file_right_num_elem():
    try:
        filename = "files/quadtree_element_error.txt"
        tkquadtree = TkQuadTree.fromFile(filename)
    except QuadTreeElementException:
        assert True

def test_tkquadtree_file_not_found():
    try:
        filename = "files/quadtree_not_found.txt"
        tkquadtree = TkQuadTree.fromFile(filename)
    except FileNotFoundError:
        assert True

def test_color_quadtree():
    filename = "files/quadtree_color"
    q = QuadTree.fromFile(filename)
    assert q.depth == 1

def test_color_large_quadtree():
    filename = "files/quadtree_extra_color.txt"
    q = QuadTree.fromFile(filename)
    assert q.depth == 3
