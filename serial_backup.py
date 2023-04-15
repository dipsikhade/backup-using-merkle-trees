import os
import hashlib
import time

class MerkleTree:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.nodes = []

    def build_tree(self):
        leaves = []
        for root, dirs, files in os.walk(self.folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, 'rb') as f:
                    content = f.read()
                    leaves.append(hashlib.sha256(content).hexdigest())
        self.nodes = [leaves]
        while len(self.nodes[-1]) > 1:
            new_layer = []
            for i in range(0, len(self.nodes[-1]), 2):
                if i+1 == len(self.nodes[-1]):
                    new_layer.append(self.nodes[-1][i])
                else:
                    left = self.nodes[-1][i]
                    right = self.nodes[-1][i+1]
                    h = hashlib.sha256(f"{left}{right}".encode()).hexdigest()
                    new_layer.append(h)
            self.nodes.append(new_layer)

    def get_root(self):
        return self.nodes[-1][0]

    def display_tree(self):
        print("Merkle Tree:")
        for i, layer in enumerate(self.nodes):
            print(f"Layer {i}: {layer}")
        print(f"Root: {self.get_root()}")

folder_path = ''
tree = MerkleTree(folder_path)
#time 
start_time = time.time()
tree.build_tree()
root = tree.get_root()
end_time = time.time()
print(f"Root Hash: {root}")
#tree.display_tree()
print(f"Time taken: {end_time - start_time:.2f} seconds")
