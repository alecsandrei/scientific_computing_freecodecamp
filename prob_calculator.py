import random


class Hat(object):

    def __init__(self, **kwargs):
        self.balls_dict = {}
        self.contents = []
        for key, value in kwargs.items():
            self.balls_dict[key] = value
            for i in range(value):
                self.contents.append(key)

    def __str__(self):
        return " ".join(self.contents)

    def draw(self, draws):
        self.sample = []
        if draws >= len(self.contents):
            self.sample = self.contents
        else:
            for i in range(draws):
                random_index = random.randint(0, len(self.contents)-1)
                self.poped = self.contents.pop(random_index)
                self.sample.append(self.poped)
        return self.sample


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    '''
    :param hat: Hat class object
    :param expected_balls: dictionary
    :param num_balls_drawn: integer
    :param num_experiments: how many to perform
    :return:
    '''

    counter = 0
    true = 0
    expected_balls_list = []
    content_copy = hat.contents[:]
    for key, value in expected_balls.items():
        for i in range(value):
            expected_balls_list.append(key)
    expected_balls_list_copy = expected_balls_list[:]
    for x in range(num_experiments):
        counter += 1
        hat.contents = content_copy[:]
        draw = hat.draw(num_balls_drawn)
        for ball in draw:
            try:
                expected_balls_list.remove(ball)
                if len(expected_balls_list) == 0:
                    true += 1
            except:
                continue
        expected_balls_list = expected_balls_list_copy[:]
    return true / num_experiments
