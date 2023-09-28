from django.db import models

time = (
    ("09","09.00 to 10.30"),
    ("1030","10.30 to 12.00"),
    ("12","12.00 to 01.30"),
    ("02","02.00 to 03.30"),
    ("330","03.30 to 05.00"),
    ("saturday","Saturday"),
    )
status = (
    ("success","Free"),
    ("danger","Engage"),
    ("warning","Temparary Free"),
    ("info","PC Complaint")
    )
pc = (
    ("pc1","PC1"),
    ("pc2","PC2"),
    ("pc3","PC3"),
    ("pc4","PC4"),
    ("pc5","PC5"),
    ("pc6","PC6"),
    ("pc7","PC7"),
    ("pc8","PC8"),
    ("pc9","PC9"),
    ("pc10","PC10"),
    ("pc11","PC11"),
    ("pc12","PC12"),
    ("pc13","PC13"),
    ("pc14","PC14"),
    ("pc15","PC15"),
    ("pc16","PC16"),
    ("pc17","PC17"),
    ("pc18","PC18"),
    ("pc19","PC19"),
    ("pc20","PC20"),
    ("pc21","PC21"),
    ("pc22","PC22"),
    ("pc23","PC23"),
    ("pc24","PC24"),
    ("pc25","PC25"),
    ("pc26","PC26"),
    ("pc27","PC27"),
    ("pc28","PC28"),
    ("pc29","PC29"),
    ("pc30","PC30"),
    )
class Systems(models.Model):
    name=models.CharField(max_length=50, blank=True)
    batch=models.CharField(choices=time, max_length=10, blank=True)
    pc=models.CharField(choices=pc, max_length=10, blank=True)
    bsd=models.DateField(blank=True, null=True)
    ebed=models.DateField(blank=True, null=True)
    status=models.CharField(choices=status, max_length=20, default="Free")
    def __str__(self):
        return self.pc
