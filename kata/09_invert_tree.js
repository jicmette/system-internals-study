function invertTree(root) {
    // Base Case: If the node is empty (null OR undefined), stop.
    if (!root) {
        return null;
    }

    // The Swap
    // I swap whatever is there (even if it's undefined)
    [root.left, root.right] = [root.right, root.left];

    // Recursion: Do the same for the children
    invertTree(root.left);
    invertTree(root.right);

    return root;
}

// Better Mock Data (Complete Nodes)
const tree = {
    val: 4,
    left: { val: 2, left: null, right: null },
    right: { val: 7, left: null, right: null }
};

console.log("Original:", JSON.stringify(tree));
console.log("Inverted:", JSON.stringify(invertTree(tree)));