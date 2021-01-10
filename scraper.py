import twint

c = twint.Config()
c.Search = "covid 19"
c.Limit = 5000
c.Store_csv = True
c.Output = "none.csv"
c.Lang = "en"
# YY-MM-DD
c.Until = "2020-12-31"
c.Since = "2020-12-01"

twint.run.Search(c)
