class MaintenanceRequest:
  def __init__(self, issueType, issueRequestDate, issueStartDate, detailDescription, userId, status):
    self.issueType = issueType
    self.issueRequestDate = issueRequestDate
    self.issueStartDate = issueStartDate
    self.detailDescription = detailDescription
    self.userId = userId
    self.status = status