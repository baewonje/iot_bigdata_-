#coding=cp949

age = 0
money = 0
choice = 0
ticket = 5
year = 3
count = 0
count1 = 0
age1 = ["����","���","û�ҳ�","����","����"]
money1= ["����",2000,3000,5000]

prompt="""
1. ����
2. ���� ���� �ſ� ī��
"""
while True:
    age=int(input("���̸� �Է��ϼ���. "))
    if 0 <= age <= 3:
        print("���ϴ� %s����̸� ����� %s�Դϴ�."%(age1[0],money1[0]))
        print("Ƽ���� �����մϴ�.")
    elif 4 <= age <= 13:
        print("���ϴ� %s����̸� ����� %d�Դϴ�."%(age1[1],money1[1]))
        choice = int(input(prompt))
        if choice == 1:
            money=int(input("����� �Է��ϼ���. "))
            if money >= money1[1]:
                print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d���� ��ȯ�մϴ�."%(money-(money1[1])))
            else:
                print("%d���� ���ڶ��ϴ�. �Է��Ͻ� %d���� ��ȯ�մϴ�."%((money1[1])-money,money))
        elif choice == 2:
            print("%d���� ���� �Ǿ����ϴ�. Ƽ���� �����մϴ�." %((money1[1])*0.9))
    elif  14 <= age <= 18:    
        print("���ϴ� %s����̸� ����� %d�Դϴ�."%(age1[2],money1[2]))
        choice = int(input(prompt))
        if choice == 1:
            money=int(input("����� �Է��ϼ���. "))
            if money >= money1[2]:
                print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d���� ��ȯ�մϴ�."%(money-(money1[2])))
            else:
                print("%d���� ���ڶ��ϴ�. �Է��Ͻ� %d���� ��ȯ�մϴ�."%((money1[2])-money,money))
        elif choice == 2:
            print("%d���� ���� �Ǿ����ϴ�. Ƽ���� �����մϴ�." %((money1[2])*0.9))
    elif  19 <= age <= 65:
        print("���ϴ� %s����̸� ����� %d�Դϴ�."%(age1[3],money1[3]))
        choice = int(input(prompt))
        if choice == 1:
            money=int(input("����� �Է��ϼ���. "))
            if money >= money1[3]:
                print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d���� ��ȯ�մϴ�."%(money-(money1[3])))
            else:
                print("%d���� ���ڶ��ϴ�. �Է��Ͻ� %d���� ��ȯ�մϴ�."%((money1[3])-money,money))
        elif choice == 2:
            if age >= 60:
                print("%d���� ���� �Ǿ����ϴ�. Ƽ���� �����մϴ�." %(((money1[3])*0.9)*0.95))
            else:
                print("%d���� ���� �Ǿ����ϴ�. Ƽ���� �����մϴ�." %((money1[3])*0.9))
    elif age > 65:
        print("���ϴ� %s����̸� ����� %s�Դϴ�."%(age1[4],money1[0]))
        print("Ƽ���� �����մϴ�.")
    if 4<=age<=65:
        count +=1
        count1 +=1
        if count == 7:
            if ticket >0:
                print("�����մϴ�. 1�ֳ� �̺�Ʈ�� ��÷ �Ǿ����ϴ�. ���� ����Ƽ���� �����մϴ�. �ܿ� ����Ƽ�� %d��"%(ticket-1))
                ticket -=1
                count = 0
        elif count1 == 4:
            if year >0:
                print("�����մϴ�. ���� ȸ���� ���� �̺�Ʈ�� ��÷�Ǽ̽��ϴ�. ���� ȸ�� ���� Ƽ���� �����մϴ�. �ܿ�Ƽ�� %d��"%(year-1))
                year-=1
                count1=0

