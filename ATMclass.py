class ATM(object):
    def __init__(CashWithdrawl,BalanceEnquiry,BalanceEnquiryRejected,CashWithdrawlUnsuccessful):
        self.CashWithdrawl=CashWithdrawl
        self.BalanceEnquiry=BalanceEnquiry
        self.BalanceEnquiryRejected=BalanceEnquiryRejected
        self.CashWithdrawlUnsuccessful=CashWithdrawlUnsuccessful

    def BalanceEnquiry(self):
        print("There is xxxxxx dollars in you account")

    def CashWithdrawl(self):
        print("Cash Withdrawn Successfully :)")

    def BalanceEnquiryRejected(self):
        print("You dont have money ...You are broke :')")

    def CashWithdrawlUnsuccessful(self):
        print("You dont have cash money... so earn some and them come back")


    
AtmMachine=ATM("CashWithdrawl,BalanceEnquiry,BalanceEnquiryRejected,CashWithdrawlUnsuccessful")
AtmMachine.BalanceEnquiryRejected()
AtmMachine.BalanceEnquiry,BalanceEnquiryRejected()
AtmMachine.CashWithdrawl()
AtmMachine.CashWithdrawl()