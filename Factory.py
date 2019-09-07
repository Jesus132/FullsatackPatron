from Api import API
from Users import users

class Factory(object):
  
  def get_Api(self, matriz):
    return API().getUsers(matriz)
  
  def get_matriz(self, matriz):
    return users().getMatr(matriz)
