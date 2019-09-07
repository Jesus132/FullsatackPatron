class users():
  def getMatr(self, aux):
    mat=[["First Name", "Last Name", "User Name", "Email", "Password"]]
    for i in aux:
      mat.append(list(i))
    return mat