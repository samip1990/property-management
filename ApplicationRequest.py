class ApplicationRequest:
  def __init__(self, userId, firstName, lastName, address, cell, ssn, moveInDate, leaseTerm,
               routingNumber, accountNumber, driverLicense, patStub, unitNumber):
    self.userId = userId
    self.firstName = firstName
    self.lastName = lastName
    self.address = address
    self.cell = cell
    self.ssn = ssn
    self.moveInDate = moveInDate
    self.leaseTerm = leaseTerm
    self.routingNumber = routingNumber
    self.accountNumber = accountNumber
    self.driverLicense = driverLicense
    self.patStub = patStub
    self.unitNumber = unitNumber