library(tmvtnorm)

mu_matrix = c(55, 40, 50, 35, 45, 30)
sigma_matrix = matrix(c(1, 1, 0, 2, -1, -1,
                        1, 16, -6, -6, -2, 12,
                        0, -6, 4, 2, -2, -5,
                        2, -6, 2, 25, 0, -17,
                        -1, -2, -2, 0, 9, -5,
                        -1, 12, -5, -17, -5, 36),
                      nrow=6, ncol=6)

# Generate scenarios
data <- rtmvt(n=1000, mean=mu_matrix, sigma=sigma_matrix, df=5,
              lower=rep(20, 6), upper=rep(60, 6))

# Write scenarios to file
write.table(format(data, digits=15, drop0trailing=F), "scenarios.txt",
            quote=F, sep="\t", eol="\n\t", col.names = F, row.names = T)
