import time

########################## class SMS_store code ##########################

class SMS_store:

    def __init__(self):
        self.message = tuple()
        self.storage = list()
    
    def add_new_arrival(self):
        self.message = tuple([False]+[input("Phone number? ")]+[time.ctime()]+[input("Contents? ")])
        self.storage.append(self.message)
    
    def message_count(self):
        return len(self.storage)
    
    def get_unread_indexes(self):
        unread_indexes = list()
        for i in self.storage:
            if i[0] == False: unread_indexes.append(self.storage.index(i))
        return unread_indexes
    
    def get_message(self,i):
        message_temp = list(self.storage[i])
        message_temp[0] = True
        tuple(message_temp)
        del self.storage[i]
        self.storage.insert(i,tuple(message_temp))
        list(message_temp)
        del message_temp[0]
        return tuple(message_temp)
        
    def delete(self,i):
        del self.storage[i]

    def clear(self):
        while len(self.storage)>0:self.storage.pop()

########################## main function code ##########################

def test_add_new_arrival(name_of_object,message_num): # n is the number of adding messages
    n=0
    while(n<message_num): # please input four example for taking four messages
        name_of_object.add_new_arrival()
        print(f"Number of messages in my_inbox : {name_of_object.message_count()}")
        n += 1

def test_get_message(name_of_object,i):
    print("<Selected message is....>")
    time.sleep(2)   #   for visual effects (you can eliminate)
    print(name_of_object.get_message(i))

def test_delete(name_of_object,i):
    print(f"<Message {i} deleted....>")
    time.sleep(2)
    name_of_object.delete(i)

def test_clear(name_of_object):
    print("<Your storage was cleaned....>")
    time.sleep(2)
    name_of_object.clear()

def test_check_storage(name_of_object):
    print("<Checking inbox storage....>")
    time.sleep(2)
    print(name_of_object.storage)

########################## test code ##########################

my_inbox = SMS_store()  # object created

test_add_new_arrival(my_inbox,4)
time.sleep(2)   #   for visual effects (you can eliminate)
test_check_storage(my_inbox)
time.sleep(2)
test_get_message(my_inbox,2)
time.sleep(2)
test_check_storage(my_inbox)
time.sleep(2)
test_delete(my_inbox,1)
time.sleep(2)
test_check_storage(my_inbox)
time.sleep(2)
test_clear(my_inbox)
time.sleep(2)
test_check_storage(my_inbox)
time.sleep(2)