from math import inf


class Node:
    def __init__(self, value=None, children=None, name=""):
        self.value = value
        self.children = children or []
        self.name = name

    def is_leaf(self):
        return self.value is not None


# ✅ Build 4-level tree correctly
A = Node(children=[
    Node(children=[
        Node(children=[
            Node(6), Node(1)
        ], name="LeftMax"),
        Node(children=[
            Node(7), Node(-3)
        ], name="RightMax"),
    ], name="LeftMin"),

    Node(children=[
        Node(children=[
            Node(-2), Node(8)
        ], name="LeftMax"),
        Node(children=[
            Node(4), Node(-6)
        ], name="RightMax")
    ], name="RightMIN")
], name="Root")

print("Alpha–beta test tree built.")


def alphabeta_iterative_with_log(root, maximizing_root=True, alpha=-inf, beta=inf):

    def label(n):
        if n.name:
            return n.name
        if n.is_leaf():
            return f"Leaf({n.value})"
        return "Node"

    def gather_leaves(n):
        """Collect ALL leaf values under a node."""
        if n.is_leaf():
            return [n.value]

        leaves = []
        for c in n.children:
            leaves.extend(gather_leaves(c))
        return leaves


    stack = [{
        "node": root,
        "maximizing": maximizing_root,
        "alpha": alpha,
        "beta": beta,
        "best": -inf if maximizing_root else inf,
        "i": 0,
        "pruned": False
    }]

    visited_leaves = []
    cutoffs = []

    while stack:
        frame = stack[-1]
        node = frame["node"]

        # ✅ LEAF
        if node.is_leaf():

            visited_leaves.append(node.value)
            value = node.value
            stack.pop()

            if not stack:
                return value, visited_leaves, cutoffs

            parent = stack[-1]

            # update parent
            if parent["maximizing"]:
                parent["best"] = max(parent["best"], value)
                parent["alpha"] = max(parent["alpha"], parent["best"])
            else:
                parent["best"] = min(parent["best"], value)
                parent["beta"] = min(parent["beta"], parent["best"])

            # 🔥 PRUNE CHECK
            if parent["beta"] <= parent["alpha"] and not parent["pruned"]:

                remaining_children = parent["node"].children[parent["i"]:]
                pruned = []

                for child in remaining_children:
                    pruned.extend(gather_leaves(child))

                cutoffs.append({
                    "at_node": label(parent["node"]),
                    "role": "MAX" if parent["maximizing"] else "MIN",
                    "after_child_index": parent["i"] - 1,
                    "alpha": parent["alpha"],
                    "beta": parent["beta"],
                    "pruned_leaves": pruned
                })

                parent["pruned"] = True
                parent["i"] = len(parent["node"].children)

            continue


        # ✅ EXPAND CHILD
        if frame["i"] < len(node.children) and not frame["pruned"]:

            child = node.children[frame["i"]]
            frame["i"] += 1

            child_max = not frame["maximizing"]

            stack.append({
                "node": child,
                "maximizing": child_max,
                "alpha": frame["alpha"],
                "beta": frame["beta"],
                "best": -inf if child_max else inf,   # ⭐ critical fix
                "i": 0,
                "pruned": False
            })

        else:
            # ✅ RETURN VALUE UP
            value = frame["best"]
            stack.pop()

            if not stack:
                return value, visited_leaves, cutoffs

            parent = stack[-1]

            if parent["maximizing"]:
                parent["best"] = max(parent["best"], value)
                parent["alpha"] = max(parent["alpha"], parent["best"])
            else:
                parent["best"] = min(parent["best"], value)
                parent["beta"] = min(parent["beta"], parent["best"])

            # 🔥 PRUNE CHECK AGAIN
            if parent["beta"] <= parent["alpha"] and not parent["pruned"]:

                remaining_children = parent["node"].children[parent["i"]:]
                pruned = []

                for child in remaining_children:
                    pruned.extend(gather_leaves(child))

                cutoffs.append({
                    "at_node": label(parent["node"]),
                    "role": "MAX" if parent["maximizing"] else "MIN",
                    "after_child_index": parent["i"] - 1,
                    "alpha": parent["alpha"],
                    "beta": parent["beta"],
                    "pruned_leaves": pruned
                })

                parent["pruned"] = True
                parent["i"] = len(parent["node"].children)

    return None, visited_leaves, cutoffs


value, visited, cutoffs = alphabeta_iterative_with_log(A)

print("Value:", value)
print("Visited leaves:", visited)
print("Cutoffs:", cutoffs)