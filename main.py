class Tree():
    def __init__(self, key):
        self.key = key
        # key აღნიშნავს ყოველ ახალ ელემენტს რომელიც შემოვა ჩვენს ხეში

        # ელემენტების დაყოფა ხდება შემდეგი მეთოდით, თუკი ახალი ელემენტი მშობელზე მეტია მაშინ წავა მარჯვენა მხარეს, ხოლო თუ ნაკლებია მარცხენა მხარეს
        # ყოველი ახალი შემოსული ელემენტი იკავებს თავის ადგილს და მისი ჩანაცვლება არ შეიძლება თუკი მას არ ამოვშლით
        self.left = None
        self.right = None

class BST(): #binary search tree
    def __init__(self):
        self.root = None
        # root არის მთვარი, პირველი შესული ელემენტი

    def __str__(self):
        return f"self.root is {str(self.root)}"


    # მონაცემის დამატება
    # აქ ვახდენთ ელემენტის დამატებას
    # 2
    def _insert(self, node, key):
        #1) მეთოდი გაეშვება მაშნ როდესაც ბალა insert1 მეო=თოდში შევა ელემენტი
        # I ელემენტი node გახდება self.root რომელიც არის None / ხოლო key აირს ყოველი ახალი გადაცემული ელემენტი
        if node is None:
        # თუკი, self.root არის None, მასში ინფორმაცია არ არის მაშინ გაეშვება ეს ბლოკი მხოლოდ
        # self.root გახდება პორველი გადაცემული ელემენტი
        #     print(f"node is {node}")
            return Tree(key)
        print(f"node.key is {node.key}")
        print(f"key is {key}")

        #2) თუკი self.root გავქვს მაშინ insert1 მეთოდი მაინც გამოიძახებს _insert2 მეთოდს
        # node გახდება 16, როგორც self.root გადავეცით მნიშვნელობა ხოლო key გახდება ახალ შემოსული ელემენტი

        # შემდგომ, key თუკი იქნება node.key ანუ მაღლა რომ node აირს იმაზე ნაკლები მაშინ გაეშვება if ბლოკი, რომელიც:

        if key < node.key:
            # node.left ჯერ გვაქვს None, რომლისთვისაც მნიშვნელობის მისანიჭებლად ვიძახებთ _insert მეთოდს ისევე, რომელიც
            # შევა პირველ if ბლოკში, რადგანაც node უდრის node.left და არის None, if ბლოკი გაეშვება და დააბრუნებს key,
            # თუკი _insert დააბრუნუბს key, შესაბამისად node.left გახდება key
            node.left = self._insert(node.left, key)
            # node.left = key
            print(f"node.left is {node.left.key}")

        # node.key აღნიშნავს mმაღლა არსებულ node-s

        # იფივემაინრად იმუშავებს იმ შემთხვევაში თუკი key-ახალი გადაცემული ელემებტი node.kye-ზე მეტი ინქბეა
        elif key > node.key:
            node.right = self._insert(node.right, key)
            print(f"node.right is {node.right.key}")
        return node




    # 1
    def insert(self, key):
        self.root = self._insert(self.root, key)
        # რიდესაც ელემენტს გდავცემთ insert1 მეთოდს იძახებს _insert2 მეთოდს მნიშვნელობის მისანიჭებლად
        print(f"self.root in insert1 is {self.root}")

#1) როგორ ხდება მონაცემის დამატება: ჯერ გადავცემთ მონაცემს, პირველი შევა insert 1 მეთოში, რომელიც გამოიძახებს self.root
# self.root კი გამოიძახებს self._insert() მეორე insert 2
# მეორე _insert გამოძახებისას გადაეცა ორი მნიშვნელობა self.root და key

# _insertის გაშვებისას გადაეცა ორი მნიშვნელობა: node რომელიც გახდა self.root-None, ა key - ახალ გადაცემიული ელემენტი


#2) თუკი self.root გვაქვს, მაშინ გაეშვება მეორე if ბლოკიც და node.left და node.right მიიღებს მნიშვნელობებს
        # თუკი self.root გავქვს მაშინ insert1 მეთოდი მაინც გამოიძახებს _insert2 მეთოდს
        # node გახდება 16, როგორც self.root გადავეცით მნიშვნელობა ხოლო key გახდება ახალ შემოსული ელემენტი
        # შემდგომ, key თუკი იქნება node.key ანუ მაღლა რომ node აირს იმაზე ნაკლები მაშინ გაეშვება if ბლოკი, რომელიც:
            # node.left ჯერ გვაქვს None, რომლისთვისაც მნიშვნელობის მისანიჭებლად ვიძახებთ _insert მეთოდს ისევე, რომელიც
            # შევა პირველ if ბლოკში, რადგანაც node უდრის node.left და არის None, if ბლოკი გაეშვება და დააბრუნებს key,
            # თუკი _insert დააბრუნუბს key, შესაბამისად node.left გახდება key



# ხოლო იმ შემთხვევაში თუკი node არ უდრის None მაშინ გადაახტება და პირდაპირ მეორე if ბლოკიდან დაიწებს მუშაობას





# #########################################################################################
# მშობლების დაბეჭვდა
# ვქმნოით ორ მეთოდს ისევე როგორც ელემენტების ჩამატებისას
# ერთ protected და ერთ public-ს
    def _print_parent(self, node, parent):
          if node:
                if parent is None:
                    print(f"{node.key} is root")
                else:
                    print(f"{node.key} parent is {parent.key}")

                self._print_parent(node.left, node)
                self._print_parent(node.right, node)

    def print_parents(self):
        self._print_parent(self.root, None)


    def _print_leaf_nodes(self, node):
        if node is not None:
            # Check if the node is a leaf node
            if node.left is None and node.right is None:
                print(f"{node.key}")

            else:
                self._print_leaf_nodes(node.left)
                self._print_leaf_nodes(node.right)




    def print_leaf_nodes(self):
        print("Leaf nodes are: ")
        self._print_leaf_nodes(self.root)




                                                                #16
                                                      #7                  #19
                                                 #5        #13       #17


bst = BST()
bst.insert(16)
print("#########################################################")
bst.insert(19)
print("#########################################################")
bst.insert(7)
print("#########################################################")
bst.insert(13)
print("#########################################################")
bst.insert(5)
print("#########################################################")
bst.insert(17)

bst.print_parents()

print("#######################################################################################")
print("homework")
bst.print_leaf_nodes()