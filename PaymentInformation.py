class PaymentInformation:
  def __init__(self, cardType, cardHolder, cardNumber, cvvNumber, paymentAmount, userId):
    self.cardType = cardType
    self.cardHolder = cardHolder
    self.cardNumber = cardNumber
    self.cvvNumber = cvvNumber
    self.paymentAmount = paymentAmount
    self.userId = userId