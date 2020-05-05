class PaymentResponse:
  def __init__(self, paymentConfirmationNumber, sucessFlag):
    self.paymentConfirmationNumber = paymentConfirmationNumber
    self.sucessFlag = sucessFlag