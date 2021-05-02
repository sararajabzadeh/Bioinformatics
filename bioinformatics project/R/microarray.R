##########Libraries#########################################
library(Biobase)
library(GEOquery)
library(limma)
library(pheatmap)
library(ggplot2)
library(reshape2)
library(plyr)
#############downloading data#########################
setwd("/Users/sara/Desktop/پروژه\ بایو")
series <- "GSE48558"
gset <- getGEO(series, GSEMatrix =TRUE, AnnotGPL=TRUE , destdir = "data/")
gset <- gset[[1]]

################Grouping data###########################
gr <- c(rep("AML" , 13),rep("Leuk" , 27),"Normal",rep("Leuk",3),
        "Normal",rep("Leuk",23),"Normal","Leuk","Normal",rep("Leuk",3),
        "Normal","Leuk",rep("Normal",4),"Leuk","Normal",rep("Leuk",2),
        rep("Normal",2),rep("Leuk",2),rep("Normal",2),"Leuk","Normal"
        ,"Leuk","Normal","Leuk","Normal","Leuk","Normal","Leuk","Normal"
        ,rep("Leuk",3),"Normal",
        rep("Leuk",3),"Normal",rep("Leuk",29),rep("Normal",7),
        rep("AML",2),"Normal",rep("AML",3),rep("Normal", 20))
################deleting Leukemias#######################
group <- which(gr!="Leuk")
gr <- gr[group]
gset <- gset[,group]

############expression######################################
ex <- exprs(gset)

##################Box plot quality control#######################
pdf("result/boxplot.pdf",width = 170)
boxplot(ex)
dev.off()

##################Heatmap quality control##########################
pdf("result/CorHeatmap.pdf",width = 20 , height = 20)
pheatmap(cor(ex), labels_row = gr , labels_col = gr)
dev.off()

######################principal component analysis quality control######################
pc <- prcomp(ex)
pdf("result/PC.pdf")
plot(pc)
plot(pc$x[,1:2])
dev.off()


#####################PCA_Scaled####################################
ex.scale <- t(scale(t(ex), scale = F))
pc <- prcomp(ex.scale)
pdf("result/PC_scaled.pdf")
plot(pc)
plot(pc$x[,1:2])
dev.off()

#################PCA for samples##################################
pcr <- data.frame(pc$rotation[,1:3] , Group = gr)
pdf("result/PCA_Samples.pdf")
ggplot(pcr,aes(PC1,PC2 , color = Group))+geom_point(size = 4) + theme_bw()
dev.off()

################Correlation control##################################
pdf("result/heatmap_cor.pdf", width = 20 , height = 20)
pheatmap(cor(ex.scale), labels_row = gr , labels_col = gr)
dev.off()

###################differential expression analysis#####################
gr <- factor(gr)
gset$description <- gr
design <- model.matrix(~ description + 0, gset)
colnames(design) <- levels(gr)
fit <- lmFit(gset, design)
cont.matrix <- makeContrasts(AML-Normal, levels=design)
fit2 <- contrasts.fit(fit, cont.matrix)
fit2 <- eBayes(fit2, 0.01)
tT <- topTable(fit2, adjust="fdr", sort.by="B", number=Inf)

tT <- subset(tT, select=c("Gene.symbol","Gene.ID","adj.P.Val","logFC"))
write.table(tT, "result/AML_Normal.txt", row.names=F, sep="\t", quote = F)

#################Gene ontology###############################################
aml.up<- subset(tT, logFC >1 & adj.P.Val<0.05)
aml.up.Gene <- unique(as.character(strsplit2(aml.up$Gene.symbol , "///")))
write.table(aml.up.Gene , file = "result/AML_Normal_UP.txt" , quote = F, row.names = F, col.names = F)


aml.down<- subset(tT, logFC < -1 & adj.P.Val<0.05)
aml.down.Gene <- unique(as.character(strsplit2(aml.down$Gene.symbol,"///")))
write.table(aml.down.Gene , file = "result/AML_Normal_DOWN.txt" , quote = F, row.names = F, col.names = F)


