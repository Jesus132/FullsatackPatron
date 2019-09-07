class API():
  def getUsers(self, aux):
    global data
    result=[]
    for i in range(len(aux)):
      result.append({'Id':aux[i][0],'First Name':aux[i][1],'Last Name':aux[i][2],'User Name':aux[i][3],'Mail':aux[i][4],'Password':aux[i][5]})
    #print({'Data':result})
    return {'Data':result}
