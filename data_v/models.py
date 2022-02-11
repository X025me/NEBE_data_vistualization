# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Candidate(models.Model):
    candidateid = models.BigIntegerField(primary_key=True)
    fullname = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    dateofbirth = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    gender = models.CharField(max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    placeofbirthid = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    addressid = models.FloatField(blank=True, null=True)
    telephone = models.FloatField(blank=True, null=True)
    email = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    constituencyid = models.ForeignKey('Hoprconstituency', models.DO_NOTHING, db_column='constituencyid', blank=True, null=True)
    regionalconstituencyid = models.ForeignKey('Regionalconstituency', models.DO_NOTHING, db_column='regionalconstituencyid', blank=True, null=True)
    kebeleid = models.ForeignKey('Kebele', models.DO_NOTHING, db_column='kebeleid')
    electionid = models.ForeignKey('Election', models.DO_NOTHING, db_column='electionid')
    politicalpartyid = models.IntegerField()
    symbolid = models.ForeignKey('Symbol', models.DO_NOTHING, db_column='symbolid')
    oldsymbolid = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    photo = models.BinaryField(blank=True, null=True)
    photocheck = models.FloatField(blank=True, null=True)
    face = models.FloatField(blank=True, null=True)
    resolution = models.FloatField(blank=True, null=True)
    version = models.FloatField(blank=True, null=True)
    profession = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    eligibility = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    documentid = models.FloatField(blank=True, null=True)
    documentnumber = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    educationid = models.IntegerField(blank=True, null=True)
    placeissued = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    dateissued = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    status = models.IntegerField()
    isactive = models.BooleanField()
    comment = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    dateofcancellation = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    dateofcancellationec = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    ballotorder = models.IntegerField(blank=True, null=True)
    dateofregistration = models.DateTimeField(blank=True, null=True)
    dateofregistrationec = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    edituser = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    editmachine = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    edituserlog = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    editmachinelog = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    editdate = models.DateTimeField(blank=True, null=True)
    editdateec = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    disability = models.BooleanField()
    june21 = models.CharField(db_column='June21', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Candidate'


class Hoprconstituency(models.Model):
    constituencyid = models.IntegerField(primary_key=True)
    constituencyname = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    contype = models.IntegerField()
    woredaid = models.ForeignKey('Woreda', models.DO_NOTHING, db_column='woredaid')
    regionid = models.ForeignKey('Region', models.DO_NOTHING, db_column='regionid')
    isactive = models.BooleanField()
    election_status = models.CharField(db_column='Election_Status', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HoPRconstituency'


class Pollingstation(models.Model):
    voterpollingstationid = models.BigIntegerField(primary_key=True)
    voterpollingstationname = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    voterpollingstationcode = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    pstype = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    kebeleid = models.ForeignKey('Kebele', models.DO_NOTHING, db_column='kebeleid')
    regionalconstituencyid = models.ForeignKey('Regionalconstituency', models.DO_NOTHING, db_column='regionalconstituencyid')
    constituencyid = models.ForeignKey(Hoprconstituency, models.DO_NOTHING, db_column='constituencyid')
    geocode = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    isactive = models.BooleanField()
    iscustom = models.BooleanField(blank=True, null=True)
    editdate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'PollingStation'


class Woreda(models.Model):
    woredaid = models.IntegerField(primary_key=True)
    woredaname = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    woredacode = models.FloatField(blank=True, null=True)
    zoneid = models.ForeignKey('Zone', models.DO_NOTHING, db_column='zoneid')
    issubcity = models.BooleanField()
    isactive = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'Woreda'


class Election(models.Model):
    electionid = models.AutoField(primary_key=True)
    electiontype = models.IntegerField()
    electionname = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    dateofelection = models.DateTimeField(blank=True, null=True)
    isactive = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'election'


class Kebele(models.Model):
    kebeleid = models.IntegerField(primary_key=True)
    kebelename = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    kebelecode = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    towncode = models.IntegerField()
    woredaid = models.ForeignKey(Woreda, models.DO_NOTHING, db_column='woredaid')
    isactive = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'kebele'


class NebeuserUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    username = models.CharField(unique=True, max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')
    full_name = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')
    is_trance = models.BooleanField()
    is_staff = models.BooleanField()
    is_checker = models.BooleanField()
    is_active = models.BooleanField()
    is_supperuser = models.BooleanField()
    is_admin = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'nebeuser_user'


class NewvoteHopresult(models.Model):
    id = models.BigAutoField(primary_key=True)
    vote = models.BigIntegerField(blank=True, null=True)
    candidate = models.OneToOneField(Candidate, models.DO_NOTHING)
    general = models.ForeignKey('NewvoteHoprgeneral', models.DO_NOTHING)
    party = models.ForeignKey('Politicatparty', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'newVote_hopresult'


class NewvoteHoprgeneral(models.Model):
    id = models.BigAutoField(primary_key=True)
    approved = models.BooleanField()
    not_aproved = models.BooleanField()
    no_of_pollingstation = models.IntegerField(blank=True, null=True)
    exclude_no_of_pollingstation = models.IntegerField(blank=True, null=True)
    q1 = models.IntegerField(blank=True, null=True)
    q2 = models.IntegerField(blank=True, null=True)
    q3 = models.IntegerField(blank=True, null=True)
    q4 = models.IntegerField(blank=True, null=True)
    q5 = models.IntegerField(blank=True, null=True)
    q6 = models.IntegerField(blank=True, null=True)
    q7 = models.IntegerField(blank=True, null=True)
    q8 = models.IntegerField(blank=True, null=True)
    q9 = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey(NebeuserUser, models.DO_NOTHING)
    hoprconstituency = models.OneToOneField(Hoprconstituency, models.DO_NOTHING, blank=True, null=True)
    region = models.ForeignKey('Region', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'newVote_hoprgeneral'


class NewvoteHoprmax(models.Model):
    id = models.BigAutoField(primary_key=True)
    result = models.ForeignKey(NewvoteHopresult, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'newVote_hoprmax'


class NewvoteHoprmemo(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    owner = models.ForeignKey(NewvoteHoprgeneral, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'newVote_hoprmemo'


class NewvoteRcgeneral(models.Model):
    id = models.BigAutoField(primary_key=True)
    approve = models.BooleanField()
    not_aproved = models.BooleanField()
    no_of_seat = models.IntegerField()
    no_of_pollingstation = models.IntegerField()
    exclude_no_of_pollingstation = models.IntegerField()
    q1 = models.IntegerField(db_column='Q1')  # Field name made lowercase.
    q2 = models.IntegerField(db_column='Q2')  # Field name made lowercase.
    q3 = models.IntegerField(db_column='Q3')  # Field name made lowercase.
    q4 = models.IntegerField(db_column='Q4')  # Field name made lowercase.
    q5 = models.IntegerField(db_column='Q5')  # Field name made lowercase.
    q6 = models.IntegerField(db_column='Q6')  # Field name made lowercase.
    q7 = models.IntegerField(db_column='Q7')  # Field name made lowercase.
    q8 = models.IntegerField(db_column='Q8')  # Field name made lowercase.
    q9 = models.IntegerField(db_column='Q9')  # Field name made lowercase.
    created_by = models.ForeignKey(NebeuserUser, models.DO_NOTHING)
    rcconstituency = models.OneToOneField('Regionalconstituency', models.DO_NOTHING, blank=True, null=True)
    region = models.ForeignKey('Region', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'newVote_rcgeneral'


class NewvoteRcmax(models.Model):
    id = models.BigAutoField(primary_key=True)
    result = models.ForeignKey('NewvoteRcresult', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'newVote_rcmax'


class NewvoteRcmemo(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    owner = models.ForeignKey(NewvoteRcgeneral, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'newVote_rcmemo'


class NewvoteRcresult(models.Model):
    id = models.BigAutoField(primary_key=True)
    vote = models.BigIntegerField()
    candidate = models.OneToOneField(Candidate, models.DO_NOTHING)
    general = models.ForeignKey(NewvoteRcgeneral, models.DO_NOTHING)
    party = models.ForeignKey('Politicatparty', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'newVote_rcresult'


class Politicatparty(models.Model):
    politicalpartyid = models.IntegerField(primary_key=True)
    politicalpartyname = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    politicalpartynameen = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    representative = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    address = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    telephone = models.FloatField(blank=True, null=True)
    isindependent = models.BooleanField()
    acronym = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    symbolid = models.ForeignKey('Symbol', models.DO_NOTHING, db_column='symbolid', blank=True, null=True)
    reason = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    oldsymbolid = models.FloatField(blank=True, null=True)
    isactive = models.BooleanField()
    edituser = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    editmachine = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    editdate = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    editdateec = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    regdate = models.FloatField(blank=True, null=True)
    regdateec = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    reguser = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'politicatparty'


class Region(models.Model):
    regionid = models.IntegerField(db_column='regionId', primary_key=True)  # Field name made lowercase.
    regionname = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    acronym = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    isactive = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'region'


class Regionalconstituency(models.Model):
    regionalconstituencyid = models.IntegerField(primary_key=True)
    regionalconstituencyname = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    woredaid = models.ForeignKey(Woreda, models.DO_NOTHING, db_column='woredaid')
    regionid = models.ForeignKey(Region, models.DO_NOTHING, db_column='regionid')
    seats = models.IntegerField()
    isactive = models.BooleanField()
    election_status = models.CharField(db_column='Election_Status', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'regionalconstituency'


class Symbol(models.Model):
    symbolid = models.IntegerField(primary_key=True)
    symbolname = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    symbolbinary = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    isactive = models.BooleanField()
    edituser = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    editmachine = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    editdate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'symbol'


class Zone(models.Model):
    zoneid = models.IntegerField(primary_key=True)
    zonename = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    zonecode = models.FloatField(blank=True, null=True)
    regionid = models.ForeignKey(Region, models.DO_NOTHING, db_column='regionid')
    isactive = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'zone'
