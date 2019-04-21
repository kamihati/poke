# coding=utf8

class Card:
    """
    牌面类。代表某张扑克牌。
    """

    # 牌面数字1-13
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    # 牌面花色
    SUITS = ["梅", "方", "红", "黑"]

    # 牌面数字，1-13
    FaceNum = None
    # 花色，梅为梅花，方为方块，红为红桃，黑为黑桃
    Suit = None

    def __init__(self, rank, suit, face_up=True):
        """
        :param rank:牌面数字
        :param suit:牌面花色
        :param face_up:
        """
        # 牌面数字
        self.rank = rank
        # 花色
        self.suit = suit
        # 是否显示牌的正面
        self.is_face_up = face_up

    def __str__(self):
        """
        打印一张牌的信息
        :return:
        """
        if self.is_face_up:
            rep = self.suit + self.rank
        else:
            rep = "XX"
        return rep

    def pic_order(self):
        """
        获取当前牌面的顺序号，牌面按梅花1-13，方块14-26，红桃27-39，黑桃40-52的顺序编号（未洗牌之前）
        :return:
        """
        if self.rank == "A":
            FaceNum = 1
        elif self.rank == "J":
            FaceNum = 11
        elif self.rank == "Q":
            FaceNum = 12
        elif self.rank == "K":
            FaceNum = 13
        else:
            FaceNum = int(self.rank)

        if self.suit == "梅":
            Suit = 1
        elif self.suit == "方":
            Suit = 2
        elif self.suit == "红":
            Suit = 3
        else:
            Suit = 4
        return  (Suit - 1) * 13 + FaceNum

    def flip(self):
        """
        翻牌方法
        :return:
        """
        self.is_face_up = not self.is_face_up



class Hand:
    """
    手牌
    """
    def __init__(self):
        # 列表存储牌手的每张手牌
        self.cards = []


    def __str__(self):
        """
        重写print方法，打印出牌手逇所有牌
        :return:
        """
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "\t"
        else:
            rep = "无牌"
        return rep

    def clear(self):
        """
        清空手里的牌
        :return:
        """
        self.cards = []

    def add(self, card):
        """
        增加牌
        :param card:
        :return:
        """
        self.cards.append(card)

    def give(self, card, other_hand):
        """
        把一张牌给其他拍手
        :param card:
        :param other_hand:
        :return:
        """
        self.cards.remove(card)
        other_hand.add(card)


class Poke(Hand):
    """
    扑克类，代表一副牌，可以看作是有52张牌的牌手，所以继承Hand类。
    """
    def populate(self):
        """
        生一副牌
        :return:
        """
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))


    def shuffle(self):
        """
        洗牌
        :return:
        """
        import random
        # 打乱牌的顺序
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=13):
        """
        发牌给玩家,每人默认13张
        :param hands:
        :param per_hand:
        :return:
        """
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.cards.remove(top_card)
                    hand.add(top_card)
                    # 上面两行代码可以使用这一行代码代替
                    # self.give(top_card, hand)
                else:
                    print("不能继续发牌了，拍已经发完了")


if __name__ == "__main__":
    print("开始玩扑克。")
    # 四个玩,包含3个真正的玩家和一个牌堆
    players = [Hand(), Hand(), Hand(), Hand()]
    poke1 = Poke()
    # 省城一副牌
    poke1.populate()
    # 洗牌
    poke1.shuffle()
    # 发给每人13张牌
    poke1.deal(players, 13)

    n = 1
    for hand in players:
        print("牌手", n, end=":")
        print(hand)
        n += 1
    input("\n按下随意键退出")
