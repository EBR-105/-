class Drink:#クラスの命名はPEP8によると大文字スタート原則。複数の単語を繋げる際も、Drink＿Colaのように大文字にする。
    pass #クラスを定義したあと何もしてないとエラー出る。しかし、まず定義だけ作っておいてあとから仕上げたいケースもある。

class Drink:
    def print_capacity(self): #print_capacityを定義（関数）　#selfはクラスから実体となったインスタンス自身を指す
        print("500ml")
    
drink = Drink() #Drinkを実体化. drinkがインスタンス。
drink.print_capacity() #print_capacityを「drink」に適用 #selfを（）内に入れるのが普通だが、実行では自動的にselfが割り当てられるので省略している

#今は引数がselfだけだが、第二引数以降を指定するのは簡単

class Drink:
    def print_capacity(self, capacity): #メソッド（関数）
        print("{}ml".format(capacity))
drink = Drink()
drink.print_capacity(50)  #ここでもselfは省略されて実行している

#今のままでは、メソッド（関数）内の引数を使ってcapacityを表示しているだけで、capacityをクラス内で保持していない
#次はインスタンス化したクラス「Drink」に「capacity」のデータ（変数）を持たせてみる

class Drink:
    def set_capacity(self, capacity): #注
        self.capacity = capacity #「set_capacity」でcapacityというデータ（変数）を保持
    def print_capacity(self):
        print("{}ml".format(self.capacity)) #「print_capacity」で保持しているデータ（変数）を出力
drink = Drink()
drink.set_capacity(5000) 
drink.print_capacity()

#ところで、注より先にprint_capacityをすると作成されていないデータをprintするためにエラーが出る。
#そこで、クラスがインスタンス化された時に実行されるメソッド（関数）、「コンストラクタ」がある。

#コンストラクタ
class Drink:
    def __init__(self, label, capacity): #インスタンスが生成される時に自動的に呼び出される特殊メソッド「コンストラクタ」
        self.label = label
        self.capacity = capacity #labelやcapacityを引数として設定。これで生成前に表示されるエラーは回避出来る。initでもselfは必要
    def print_info(self):
        print("{} {}ml".format(self.label, self.capacity))
drink = Drink("wine", 800)
drink.print_info()
drink2 = Drink("cola", 500)
drink2.print_info()

#しかしこのままだと、変えてはいけないデータを作成できていない。
#変えていいデータ→飲み物の種類、内容量　　変えてはいけないデータ→容器がペットボトル、開け方がキャップを開ける　　など
#そのため、データへのアクセスを制限したり、関数の呼び出しを制限する「アクセス制限」を実装する。
#例えば
class Drink:
    def __init__(self, label, capacity): 
        self.label = label
        self.capacity = capacity  
    def print_info(self):
        print("{} {}ml".format(self.label, self.capacity))
drink = Drink("wine", 800)
drink.print_info()
drink2 = Drink("cola", 500)
drink2.print_info() #ここまではさっきと同じ
drink.label = "coffee"
drink.capacity = 500
drink.print_info() #こうすると書き換えられてしまう


#カプセル化によってプライベート変数を作成
class Drink:
    def __init__(self, label, capacity): 
        self.label = label
        self._capacity = capacity #PEP8ではこのように、プライベートにしたい変数の前に_を一つだけ付けて、#でドキュメントでその旨を残す事を推奨している
    def print_info(self):
        print("{} {}ml".format(self.label, self._capacity)) #ここにも
drink = Drink("wine", 800)
drink.print_info()
drink2 = Drink("cola", 500)
drink2.print_info()

#継承
#コーラとワインを例にして考える。共通項目は商品名と内容量。そこにコーラはカテゴリ名、製造販売者。ワインには色とアルコール度数を付与したい。
#まずは共通項目である「親クラス」を記述し、あとから「子クラス」を作る
class Drink:
    def __init__(self, label, capacity): 
        self.label = label
        self.capacity = capacity 
    def print_info(self):
        print("{} {}ml".format(self.label, self.capacity)) #ここまでは親クラス
        
class Wine(Drink): #class 子クラス(親クラス):　で継承。まず最初に親クラスを定義する必要がある
    def __init__(self, label, capacity, color, alcohol):
        super().__init__(label, capacity) #super()が親クラスを指す。つまりクラス「Drink」のコンストラクタを使うと宣言
        self.color = color #子クラスで__init__宣言の時に親クラスから引っ張ってこれないものはこのように個別で追加
        self.alcohol = alcohol
class Soft_Drink(Drink):
    def __init__(self, label, capacity, category, vendor):
        super().__init__(label, capacity)
        self.category = category
        self.vendor = vendor
wine = Wine("wine", 800, "red", "10")
cola = Soft_Drink("cola", 500, "soda", "coca cola")
wine.print_info()
cola.print_info()

#このままだとせっかく追加した情報が表示されていない。そこでprintを再定義する
class Drink:
    def __init__(self, label, capacity): 
        self.label = label
        self.capacity = capacity 
    def print_info(self):
        print("{} {}ml".format(self.label, self.capacity)) #ここまでは親クラス
        
class Wine(Drink): 
    def __init__(self, label, capacity, color, alcohol):
        super().__init__(label, capacity) 
        self.color = color 
        self.alcohol = alcohol
    
    def print_info(self): #print_info()メソッド（関数）をワイン用に再定義
        print("{} {}ml".format(self.label, self.capacity))
        print("ワインの色{} アルコール度数{}".format(self.color, self.alcohol))
        
class Soft_Drink(Drink):
    def __init__(self, label, capacity, category, vendor):
        super().__init__(label, capacity)
        self.category = category
        self.vendor = vendor
    
    def print_info(self): #print_info()メソッド（関数）をコーラ用に再定義
        print("{} {}ml".format(self.label, self.capacity))
        print("種類{} 販売者{}".format(self.category, self.vendor))
        
wine = Wine("wine", 800, "red", "10")
cola = Soft_Drink("cola", 500, "soda", "coca cola")
wine.print_info()
cola.print_info()

