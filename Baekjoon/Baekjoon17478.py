n = int(input())

print("��� �� ��ǻ�Ͱ��а� �л��� ������ �������� ã�ư� ������.")


def recursive_question(num):
  global n
  sun = "____"
  if num == n:
    print(sun*num+"\"����Լ��� ������?\"")
    print(sun*num+"\"����Լ��� �ڱ� �ڽ��� ȣ���ϴ� �Լ����\"")
    print(sun*num+"��� �亯�Ͽ���.")
    return
  print(sun*num+"\"����Լ��� ������?\"")
  print(sun*num+"\"�� ����. �������� �� �� ����⿡ �̼��� ��� ������ ����� ������ �־���.\n"+sun*num+"���� ������� ��� �� ���ο��� ������ ������ �߰�, ��� �����Ӱ� ����� �־���.\n"+sun*num+ "���� ���� ��κ� �ǾҴٰ� �ϳ�. �׷��� ��� ��, �� ���ο��� �� ���� ã�ƿͼ� ������.\"")
  recursive_question(num+1)
  print(sun*num+"��� �亯�Ͽ���.")
  

recursive_question(0)