import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_utils import enable_executor_hook


def pair_includes_ancestor_and_descendant_of_m(possible_anc_or_desc_0,
                                               possible_anc_or_desc_1, middle):
    # TODO - you fill in here.
    def is_descendent(anc, dec):
        while anc:
            if anc == dec:
                return True
            elif anc.data < dec.data:
                anc = anc.right
            elif anc.data > dec.data:
                anc = anc.left
        return False

    print("possible_anc_or_desc_0.data: ", possible_anc_or_desc_0.data)
    print("possible_anc_or_desc_1.data: ", possible_anc_or_desc_1.data)
    print("middle.data: ", middle.data)
    if ((possible_anc_or_desc_0.data == possible_anc_or_desc_1.data) or
            (possible_anc_or_desc_0.data == middle.data)
            or (possible_anc_or_desc_1.data == middle.data)):
        return False

    return ((is_descendent(possible_anc_or_desc_0, middle)
        and is_descendent(middle, possible_anc_or_desc_1))
        or (is_descendent(possible_anc_or_desc_1, middle)
        and is_descendent(middle, possible_anc_or_desc_0)))




@enable_executor_hook
def pair_includes_ancestor_and_descendant_of_m_wrapper(
        executor, tree, possible_anc_or_desc_0, possible_anc_or_desc_1,
        middle_idx):
    candidate0 = must_find_node(tree, possible_anc_or_desc_0)
    candidate1 = must_find_node(tree, possible_anc_or_desc_1)
    middle_node = must_find_node(tree, middle_idx)

    return executor.run(
        functools.partial(pair_includes_ancestor_and_descendant_of_m,
                          candidate0, candidate1, middle_node))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "descendant_and_ancestor_in_bst.py",
            'descendant_and_ancestor_in_bst.tsv',
            pair_includes_ancestor_and_descendant_of_m_wrapper))
