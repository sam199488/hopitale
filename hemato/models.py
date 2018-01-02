from __future__ import unicode_literals

from django.db import models

class AtcdCher(models.Model):
    idatcd_cher = models.AutoField(primary_key=True)
    n1 = models.TextField(blank=True, null=True)
    annee1 = models.DateField(blank=True, null=True)
    n2 = models.TextField(blank=True, null=True)
    annee2 = models.DateField(blank=True, null=True)
    n3 = models.TextField(blank=True, null=True)
    anne3 = models.DateField(blank=True, null=True)
    commentaires = models.TextField(blank=True, null=True)
    is_compli_throm = models.IntegerField(blank=True, null=True) #deleted
    compli_throm = models.TextField(blank=True, null=True) #deleted
    atcd_fam = models.IntegerField(blank=True, null=True)
    photo = models.TextField(blank=True, null=True)
    patient_idpatient = models.ForeignKey('Patient', models.DO_NOTHING, db_column='patient_idpatient')

    class Meta:
        managed = True
        db_table = 'atcd_cher'
        unique_together = (('idatcd_cher', 'patient_idpatient'),)


class BilanBiologique(models.Model):
    idbilan_biologique = models.AutoField(primary_key=True)
    date = models.DateField(blank=True, null=True)

    actvite_antixa_hbpm = models.IntegerField(blank=True, null=True)
    actvite_antixa_fondaparinux = models.IntegerField(blank=True, null=True)
    actvite_antixa_rivaroxaban = models.IntegerField(blank=True, null=True)
    actvite_antixa_apixaban = models.IntegerField(blank=True, null=True)
    actvite_antixa_dabigatran = models.IntegerField(blank=True, null=True)
    actvite_antixa_edoxaban = models.IntegerField(blank=True, null=True)
    actvite_antixa_hnf = models.IntegerField(blank=True, null=True)

    aspi_test  = models.CharField(max_length=100, blank=True, null=True)
    adp_test  = models.CharField(max_length=100, blank=True, null=True)
    trap_test  = models.CharField(max_length=100, blank=True, null=True)
    vasp_test  = models.CharField(max_length=100, blank=True, null=True)

    neutrophiles = models.IntegerField(blank=True, null=True)
    hct = models.IntegerField(blank=True, null=True)
    globules_blancs = models.FloatField(blank=True, null=True)
    hb = models.FloatField(blank=True, null=True)
    reticulocytes = models.FloatField(blank=True, null=True)
    plaquettes = models.FloatField(blank=True, null=True)
    creatine = models.FloatField(blank=True, null=True)
    clairance_creatinine_cockcroft = models.FloatField(blank=True, null=True)
    mdrd = models.FloatField(db_column='MDRD', blank=True, null=True)  # Field name made lowercase.
    asat = models.FloatField(blank=True, null=True)
    alat = models.FloatField(blank=True, null=True)
    ggt = models.FloatField(blank=True, null=True)
    pal = models.FloatField(blank=True, null=True)
    bilirubine_totale = models.FloatField(blank=True, null=True)
    bilirubine_conjuguee = models.FloatField(blank=True, null=True)
    ldh = models.FloatField(blank=True, null=True)
    homocysteine = models.FloatField(blank=True, null=True)
    vitamine_d = models.FloatField(blank=True, null=True)
    crp = models.FloatField(blank=True, null=True)
    c3 = models.FloatField(blank=True, null=True)
    c4 = models.FloatField(blank=True, null=True)
    ch50 = models.FloatField(blank=True, null=True)
    tp = models.FloatField(blank=True, null=True)
    tca = models.CharField(max_length=45, blank=True, null=True)
    fibrinogene = models.FloatField(blank=True, null=True)
    antithrombine = models.FloatField(blank=True, null=True)
    antithrombine_ag = models.FloatField(blank=True, null=True)
    antithrombine_controle = models.FloatField(blank=True, null=True) #deleted
    antithrombine_controle_date = models.DateField(blank=True, null=True) #deleted
    protein_s = models.FloatField(blank=True, null=True)
    protein_s_ag = models.FloatField(blank=True, null=True)
    protein_s_controle = models.FloatField(blank=True, null=True) #deleted
    protein_s_controle_date = models.DateField(blank=True, null=True) #deleted
    protein_c = models.FloatField(blank=True, null=True)
    protein_c_ag = models.FloatField(blank=True, null=True)
    protein_c_controle = models.FloatField(blank=True, null=True) #deleted
    protein_c_controle_date = models.DateField(blank=True, null=True) #deleted
    f_v_leiden = models.CharField(max_length=45, blank=True, null=True)
    fiig20210a = models.CharField(max_length=45, blank=True, null=True)
    ppl_clotting_time = models.FloatField(blank=True, null=True)
    lag_time = models.FloatField(blank=True, null=True)
    ttpeak = models.CharField(max_length=45, blank=True, null=True)
    peak = models.CharField(max_length=45, blank=True, null=True)
    mri = models.FloatField(blank=True, null=True)
    etp = models.FloatField(blank=True, null=True)
    ct = models.FloatField(blank=True, null=True)
    cft = models.FloatField(blank=True, null=True)
    alpha = models.FloatField(blank=True, null=True)
    ma = models.FloatField(blank=True, null=True) #now it is named MCF
    fviii = models.FloatField(blank=True, null=True)
    fvw = models.FloatField(blank=True, null=True)
    thromboincode = models.TextField(max_length=500, blank = True, null = True)
    jak2_v617f = models.CharField(max_length=45, blank=True, null=True)
    jak2_exon12 = models.CharField(max_length=45, blank=True, null=True)
    mpl = models.CharField(max_length=45, blank=True, null=True)
    calr2 = models.CharField(max_length=45, blank=True, null=True)
    acc_la = models.IntegerField(blank=True, null=True)
    acl_lgg = models.FloatField(blank=True, null=True)
    acl_lgm = models.FloatField(blank=True, null=True)
    ab2gp1_lgg = models.FloatField(blank=True, null=True)
    ab2gp1_lgm = models.FloatField(blank=True, null=True)
    drvvt = models.FloatField(blank=True, null=True)
    antipe_g = models.CharField(max_length=45, blank=True, null=True)
    antipe_m = models.CharField(max_length=45, blank=True, null=True)
    aav_g = models.CharField(max_length=45, blank=True, null=True)
    antips_pt_g = models.CharField(db_column='antips-pt_g', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    antips_pt_m = models.CharField(db_column='antips-pt_m', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    aan = models.IntegerField(blank=True, null=True)
    type_if = models.CharField(max_length=45, blank=True, null=True)
    ect_type = models.CharField(max_length=45, blank=True, null=True)
    antidna = models.CharField(max_length=4, blank=True, null=True)
    anti_ccp = models.IntegerField(blank=True, null=True)
    fr_i = models.IntegerField(blank=True, null=True)
    anca = models.IntegerField(blank=True, null=True)
    anti_pr3 = models.IntegerField(blank=True, null=True)
    anti_mpo = models.IntegerField(blank=True, null=True)
    eps = models.FloatField(blank=True, null=True)
    anticorps_antithy = models.IntegerField(blank=True, null=True)
    trak = models.IntegerField(blank=True, null=True)
    antitpo = models.IntegerField(blank=True, null=True)
    antithyroglobuline = models.IntegerField(blank=True, null=True)
    antitransglutaminases = models.IntegerField(blank=True, null=True)

    #thromboincode can take 3 values 1 = Absence  2 = Hétérozygote   3 = Homozygote
    thromboincode_f12 = models.IntegerField(blank=True, null=True)
    thromboincode_abo_rs8176719 = models.IntegerField(blank=True, null=True)
    thromboincode_abo_rs7853989 = models.IntegerField(blank=True, null=True)
    thromboincode_abo_rs8176743 = models.IntegerField(blank=True, null=True)
    thromboincode_abo_rs8176750 = models.IntegerField(blank=True, null=True)
    thromboincode_f13 = models.IntegerField(blank=True, null=True)
    thromboincode_f5 = models.IntegerField(blank=True, null=True)
    thromboincode_serpin_c1 = models.IntegerField(blank=True, null=True)
    thromboincode_f12_prothrombin = models.IntegerField(blank=True, null=True)
    thromboincode_f5_HongKong = models.IntegerField(blank=True, null=True)
    thromboincode_f5_Cambridge = models.IntegerField(blank=True, null=True)
    thromboincode_f5_leiden = models.IntegerField(blank=True, null=True)




    patient_idpatient = models.ForeignKey('Patient', models.DO_NOTHING, db_column='patient_idpatient')

    class Meta:
        managed = True
        db_table = 'bilan_biologique'
        unique_together = (('idbilan_biologique', 'patient_idpatient'),)


class ConsultationSuivi(models.Model):
    idconsultation_suivi = models.AutoField(primary_key=True)
    date_consultation = models.DateField(blank=True, null=True)
    traitemnt_antithrom_enCours = models.IntegerField(blank=True, null=True)
    tae_lequel = models.CharField(max_length=100, blank=True, null=True)
    episode_throm = models.IntegerField(blank=True, null=True)
    episode_hemo = models.IntegerField(blank=True, null=True)
    episode_hemo_lequel = models.CharField(max_length=100, blank=True, null=True)
    gravite_hemoragie = models.CharField(max_length=100, blank=True, null=True)
    date_souvenue = models.DateField(blank=True, null=True)
    compli_traitement_anticoagulant = models.CharField(max_length=200, blank=True, null=True)
    manifNouvPatho = models.CharField(max_length=200, blank=True, null=True)
    grossesEnCours = models.CharField(max_length=5, blank=True, null=True)
    commentaires = models.CharField(max_length=5, blank=True, null=True)
    patient_idpatient = models.ForeignKey('Patient', models.DO_NOTHING, db_column='patient_idpatient')

    class Meta:
        managed = True
        db_table = 'consultationSuivi'
        unique_together = (('idconsultation_suivi', 'patient_idpatient'),)


class ExamenArret(models.Model):
    idexamen_arret = models.AutoField(primary_key=True)
    lag_time = models.FloatField(blank=True, null=True)
    ttpeak = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    mri = models.FloatField(blank=True, null=True)
    etp = models.FloatField(blank=True, null=True)
    ct = models.FloatField(blank=True, null=True)
    cft = models.FloatField(blank=True, null=True)
    alpha = models.FloatField(blank=True, null=True)
    ma = models.FloatField(blank=True, null=True)
    glob_bla = models.FloatField(blank=True, null=True)
    hb = models.FloatField(blank=True, null=True)
    plaquettes = models.FloatField(blank=True, null=True)
    fibrinogene = models.FloatField(blank=True, null=True)
    fviii = models.FloatField(blank=True, null=True)
    fvw = models.FloatField(blank=True, null=True)
    ddimeres = models.FloatField(blank=True, null=True)
    patient_idpatient = models.ForeignKey('Patient', models.DO_NOTHING, db_column='patient_idpatient')

    class Meta:
        managed = True
        db_table = 'examen_arret'
        unique_together = (('idexamen_arret', 'patient_idpatient'),)



class EpisodeT(models.Model):
    idepisode_t = models.AutoField(primary_key=True)
    date_imagerie = models.DateField(blank=True, null=True)
    sequelles = models.TextField(blank=True, null=True)
    fac_dec_3m = models.TextField(blank=True, null=True)
    med_episode_t = models.CharField(max_length=45, blank=True, null=True)
    med_episode = models.CharField(max_length=45, blank=True, null=True)
    patient_idpatient = models.ForeignKey('Patient', models.DO_NOTHING, db_column='patient_idpatient')

    class Meta:
        managed = True
        db_table = 'episode_t'
        unique_together = (('idepisode_t', 'patient_idpatient'),)


class Episodes(models.Model):
    idepisodes = models.AutoField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    veine = models.CharField(max_length=45, blank=True, null=True)
    artere = models.CharField(max_length=45, blank=True, null=True)
    facteur_declenchants = models.CharField(max_length=45, blank=True, null=True)
    duree = models.IntegerField(blank=True, null=True)
    type_trait = models.CharField(max_length=45, blank=True, null=True)
    #added ..
    aucun = models.IntegerField(blank=True, null=True)
    tamt_arret_depuis = models.IntegerField(blank=True, null=True)
    antiagregants_plaq = models.CharField(max_length=20, blank=True, null=True)
    dernier_val_antxa = models.IntegerField(blank=True, null=True)
    date_dva = models.DateField(blank=True, null=True)
    heparine = models.IntegerField(blank=True, null=True)
    avk = models.IntegerField(blank=True, null=True)
    dernier_inr = models.CharField(max_length=45, blank=True, null=True)
    date_di = models.DateField(blank=True, null=True)
    aod = models.IntegerField(blank=True, null=True)
    comp_trait = models.IntegerField(blank=True, null=True)


    patient_idpatient = models.ForeignKey('Patient', models.DO_NOTHING, db_column='patient_idpatient')


    class Meta:
        managed = True
        db_table = 'episodes'
        unique_together = (('idepisodes', 'patient_idpatient'),)


class FacteurResique(models.Model):
    idfacteur_risque = models.AutoField(primary_key=True)
    poids = models.FloatField(blank=True, null=True)
    taille = models.FloatField(blank=True, null=True)
    bmi = models.FloatField(db_column='BMI', blank=True, null=True)  # Field name made lowercase.
    atcd_infractus_myocard = models.IntegerField(db_column='ATCD_infractus_myocard', blank=True, null=True)  # Field name made lowercase.
    atcd_familiaux_mtev = models.IntegerField(db_column='ATCD_familiaux_MTEV', blank=True, null=True)  # Field name made lowercase.
    atcd_personnels_mtev = models.IntegerField(db_column='ATCD_personnels_MTEV', blank=True, null=True)  # Field name made lowercase.
    avc_ischemique = models.IntegerField(db_column='AVC_ischemique', blank=True, null=True)  # Field name made lowercase.
    arteriopathie_mi = models.IntegerField(db_column='arteriopathie_MI', blank=True, null=True)  # Field name made lowercase.
    coronaropathie = models.IntegerField(blank=True, null=True)
    diabete = models.IntegerField(blank=True, null=True)
    hta = models.IntegerField(db_column='HTA', blank=True, null=True)  # Field name made lowercase.
    hyperlipid_mie = models.IntegerField(db_column='hyperlipid\xe9mie', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    hypo_albuminemie = models.IntegerField(blank=True, null=True)
    insuffisance_cardiaque = models.IntegerField(blank=True, null=True)
    pilule = models.CharField(max_length=3, blank=True, null=True)
    stent_coronaore = models.IntegerField(blank=True, null=True)
    trouble_rythme_cardiaque = models.IntegerField(blank=True, null=True)
    tabac = models.IntegerField(blank=True, null=True)
    varices = models.IntegerField(blank=True, null=True)
    maladie_auto_immune = models.CharField(max_length=70, blank=True, null=True)
    maladie_inflamatoire_c_i = models.CharField(max_length=70, blank=True, null=True)
    syndrome_drepanocytaire_majeur = models.CharField(max_length=70, blank=True, null=True)
    autre_hemoglobinopathie = models.CharField(max_length=70, blank=True, null=True)
    vih = models.IntegerField(blank=True, null=True)
    vih_cd4 = models.IntegerField(db_column='VIH_CD4', blank=True, null=True)  # Field name made lowercase.
    vih_cv = models.IntegerField(db_column='VIH_CV', blank=True, null=True)  # Field name made lowercase.
    patient_idpatient = models.ForeignKey('Patient', models.DO_NOTHING, db_column='patient_idpatient')

    class Meta:
        managed = True
        db_table = 'facteur_resique'
        unique_together = (('idfacteur_risque', 'patient_idpatient'),)


class GrossessInfertilite(models.Model):
    idgrossess_infertilite = models.AutoField(primary_key=True)
    contr_oestr = models.IntegerField(blank=True, null=True)
    duree_co = models.IntegerField(blank=True, null=True)
    date_debut_co = models.DateField(blank=True, null=True)
    pilule_co = models.CharField(max_length=45, blank=True, null=True)
    traitement_sub_men = models.IntegerField(blank=True, null=True)
    traitement_sub_men_lesquel = models.CharField(max_length=45, blank=True, null=True)
    date_tsm = models.DateField(blank=True, null=True)
    endometriose = models.IntegerField(blank=True, null=True)# to be deleted
    infertilit_prim = models.IntegerField(db_column='infertilit\xe9_prim', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    raison_fiv = models.CharField(max_length=45, blank=True, null=True)
    nb_embrayons_trans = models.IntegerField(blank=True, null=True)
    embr_cong = models.IntegerField(blank=True, null=True)
    embrayons = models.IntegerField(blank=True, null=True)
    nb_fiv_av_gross = models.IntegerField(blank=True, null=True)
    spontanee = models.IntegerField(blank=True, null=True)
    fiv_icsi = models.IntegerField(blank=True, null=True)
    stimul_clomid = models.IntegerField(blank=True, null=True)
    delai_conception = models.IntegerField(blank=True, null=True)
    ras = models.IntegerField(blank=True, null=True)
    perte_foetal_terme = models.IntegerField(blank=True, null=True)
    terme_sa1 = models.CharField(max_length=45, blank=True, null=True)
    diab = models.IntegerField(blank=True, null=True)
    term_sa2 = models.CharField(max_length=45, blank=True, null=True)
    hta = models.IntegerField(blank=True, null=True)
    term_sa3 = models.CharField(max_length=45, blank=True, null=True)
    rciu = models.IntegerField(blank=True, null=True)
    term_sa4 = models.CharField(max_length=45, blank=True, null=True)
    pe = models.IntegerField(blank=True, null=True)
    term_sa5 = models.CharField(max_length=45, blank=True, null=True)
    hellp = models.IntegerField(blank=True, null=True)
    term_sa6 = models.CharField(max_length=45, blank=True, null=True)
    hrp = models.IntegerField(blank=True, null=True)
    term_sa7 = models.CharField(max_length=45, blank=True, null=True)
    thromb_maternelle_pgiu = models.CharField(max_length=45, blank=True, null=True)
    thromb_site = models.CharField(max_length=45, blank=True, null=True)
    term_sa8 = models.CharField(max_length=45, blank=True, null=True)
    apgar = models.CharField(max_length=45, blank=True, null=True)
    poids_naiss = models.IntegerField(blank=True, null=True)
    complication_neo = models.IntegerField(blank=True, null=True)
    complication_neo_lesquel = models.CharField(max_length=45, blank=True, null=True) #KO
    traitement_pgiu = models.IntegerField(blank=True, null=True)
    tpgiu_avgross = models.IntegerField(blank=True, null=True)

    aspirine = models.IntegerField(blank=True, null=True)
    aspirine_dose = models.IntegerField(blank=True, null=True)
    hbpm = models.IntegerField(blank=True, null=True)
    hbpm_dose = models.IntegerField(blank=True, null=True)
    iso = models.IntegerField(blank=True, null=True)
    iso_dose = models.IntegerField(blank=True, null=True)
    curatif = models.IntegerField(blank=True, null=True)
    curatif_dose = models.IntegerField(blank=True, null=True)
    uvedose = models.IntegerField(blank=True, null=True)
    uvedose_dose = models.IntegerField(blank=True, null=True)
    prednisone = models.IntegerField(blank=True, null=True)
    prednisone_dose = models.IntegerField(blank=True, null=True)
    dose_dose = models.IntegerField(blank=True, null=True)
    progsterion = models.IntegerField(blank=True, null=True)
    progsterion_dose = models.IntegerField(blank=True, null=True)
    hydroxychloroquine = models.IntegerField(blank=True, null=True)
    hydroxychloroquine_dose = models.IntegerField(blank=True, null=True)


    plac_gross_poids = models.IntegerField(blank=True, null=True)
    hem_dec_base = models.IntegerField(blank=True, null=True)
    nidf = models.IntegerField(blank=True, null=True)
    siege_nidf = models.CharField(max_length=45, blank=True, null=True)
    infarctus = models.IntegerField(blank=True, null=True)
    signe_infractus = models.CharField(max_length=45, blank=True, null=True)
    nb_infractus = models.IntegerField(blank=True, null=True)
    thromb_art = models.IntegerField(blank=True, null=True)
    chorioamniotite = models.IntegerField(blank=True, null=True)
    villites = models.IntegerField(blank=True, null=True)
    intervillites = models.IntegerField(blank=True, null=True)
    vasculopathie_throm = models.IntegerField(blank=True, null=True)
    caryotype_foetus = models.IntegerField(blank=True, null=True)
    malformation_foetus = models.IntegerField(blank=True, null=True)
    maladie_autoimmune = models.IntegerField(blank=True, null=True)
    maladie_autoimmune_lesquel = models.CharField(max_length=45, blank=True, null=True)
    thrombose_art = models.IntegerField(blank=True, null=True)
    date_ta = models.DateField(blank=True, null=True)
    nb_ta = models.IntegerField(blank=True, null=True)
    site_ta = models.CharField(max_length=45, blank=True, null=True)
    thrombose_veineuse = models.IntegerField(blank=True, null=True)
    date_tv = models.DateField(blank=True, null=True)
    nb_tv = models.IntegerField(blank=True, null=True)
    site_tv = models.CharField(max_length=45, blank=True, null=True)
    patient_idpatient = models.ForeignKey('Patient', models.DO_NOTHING, db_column='patient_idpatient')

    class Meta:
        managed = True
        db_table = 'grossess_infertilite'
        unique_together = (('idgrossess_infertilite', 'patient_idpatient'),)


class PathologieMalain(models.Model):
    idpathologie_malain = models.AutoField(primary_key=True)
    caractere = models.CharField(max_length=45, blank=True, null=True)
    site_initiale = models.CharField(max_length=45, blank=True, null=True)
    stade = models.CharField(max_length=45, blank=True, null=True)
    statut_evolutif = models.CharField(max_length=45, blank=True, null=True)
    temp_ecoule = models.CharField(max_length=45, blank=True, null=True)
    score_ecog = models.IntegerField(blank=True, null=True)
    indice_perf_ocog = models.CharField(max_length=45, blank=True, null=True)
    pathologie_malaincol = models.CharField(max_length=45, blank=True, null=True)
    patient_idpatient = models.ForeignKey('Patient', models.DO_NOTHING, db_column='patient_idpatient')

    class Meta:
        managed = True
        db_table = 'pathologie_malain'
        unique_together = (('idpathologie_malain', 'patient_idpatient'),)


class Patient(models.Model):
    idpatient = models.AutoField(primary_key=True)
    ipp = models.CharField(max_length=45)
    nompatient = models.CharField(max_length=45)
    prenompatient = models.CharField(max_length=45)
    datenaissance = models.DateField(blank=True, null=True)
    groupesanguin = models.CharField(max_length=5, blank=True, null=True)
    telephonepatient = models.CharField(max_length=15, blank=True, null=True)
    hopitale = models.IntegerField(blank=True, null=True) #1 tenon #2 st antoine #3 pitie salpetriere
    servicereference = models.CharField(max_length=45, blank=True, null=True)
    nommedecinreferent = models.CharField(max_length=45, blank=True, null=True)
    prenommedcinreferent = models.CharField(max_length=45, blank=True, null=True)
    telephonemedecinreferent = models.CharField(max_length=15, blank=True, null=True)
    type_consultation = models.CharField(max_length=15, blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    date_consultation = models.CharField(max_length=45, blank=True, null=True)
    premiere_con = models.IntegerField(blank=True, null=True)
    suivi = models.IntegerField(blank=True, null=True)
    consentement_eclaire = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'patient'

    def __str__(self):  # __unicode__ on Python 2
        return self.nompatient+" "+self.prenompatient


class Recommandation(models.Model):
    idrecommandation = models.AutoField(primary_key=True)
    type_traitement = models.CharField(max_length=45, blank=True, null=True)
    date_debut = models.DateField(blank=True, null=True)
    date_fin = models.DateField(blank=True, null=True)
    encours = models.IntegerField(blank=True, null=True)
    inr = models.FloatField(blank=True, null=True)
    act_antixa = models.FloatField(blank=True, null=True)
    concentration_xeap = models.FloatField(blank=True, null=True)
    heure_der_prise = models.TimeField(blank=True, null=True)
    heur_prelevemnt = models.TimeField(blank=True, null=True)
    hypera_rsap = models.IntegerField(blank=True, null=True)
    trait = models.CharField(max_length=45, blank=True, null=True)
    lag_time = models.FloatField(blank=True, null=True)
    ttpeak = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    mri = models.FloatField(blank=True, null=True)
    etp = models.FloatField(blank=True, null=True)
    ct = models.FloatField(blank=True, null=True)
    cft = models.FloatField(blank=True, null=True)
    alpha = models.FloatField(blank=True, null=True)
    ma = models.FloatField(blank=True, null=True)
    glob_bla = models.FloatField(blank=True, null=True)
    hb = models.FloatField(blank=True, null=True)
    plaquettes = models.FloatField(blank=True, null=True)
    fibrinogene = models.FloatField(blank=True, null=True)
    fviii = models.FloatField(blank=True, null=True)
    fvw = models.FloatField(blank=True, null=True)
    ddimeres = models.FloatField(blank=True, null=True)
    complication_hemo = models.FloatField(blank=True, null=True)
    type_com_hemo = models.CharField(max_length=45, blank=True, null=True)
    patient_idpatient = models.ForeignKey(Patient, models.DO_NOTHING, db_column='patient_idpatient')

    class Meta:
        managed = True
        db_table = 'recommandation'
        unique_together = (('idrecommandation', 'patient_idpatient'),)


class TraitementAnt(models.Model):
    id = models.AutoField(primary_key=True)
    methotrexate = models.IntegerField(blank=True, null=True)
    number_6_mercaptopurine = models.IntegerField(db_column='6_mercaptopurine', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    purinethole = models.IntegerField(blank=True, null=True)
    fludarabine = models.IntegerField(blank=True, null=True)
    number_5fu = models.IntegerField(db_column='5fu', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    cytarbine = models.IntegerField(blank=True, null=True)
    hydrea = models.IntegerField(blank=True, null=True)
    asparginase = models.IntegerField(blank=True, null=True)
    chlorambucil = models.IntegerField(blank=True, null=True)
    melphalan = models.IntegerField(blank=True, null=True)
    cyclophosphamide = models.IntegerField(blank=True, null=True)
    nitroso_urees = models.IntegerField(blank=True, null=True)
    derives_platine = models.IntegerField(blank=True, null=True)
    mitomycine = models.IntegerField(blank=True, null=True)
    doxorubicine = models.IntegerField(blank=True, null=True)
    mitoxanthone = models.IntegerField(blank=True, null=True)
    etoposide = models.IntegerField(blank=True, null=True)
    vincristine = models.IntegerField(blank=True, null=True)
    vinblastatine = models.IntegerField(blank=True, null=True)
    taxanes = models.IntegerField(blank=True, null=True)
    rituximab = models.IntegerField(blank=True, null=True)
    autre_immunotherapie = models.CharField(max_length=60, blank=True, null=True)
    daratumumab = models.IntegerField(blank=True, null=True)
    bleomycine = models.IntegerField(blank=True, null=True)
    anastrozole = models.IntegerField(blank=True, null=True)
    exemestane = models.IntegerField(blank=True, null=True)
    letrozole = models.IntegerField(blank=True, null=True)
    fulvestrant = models.IntegerField(blank=True, null=True)
    raloxifene = models.IntegerField(blank=True, null=True)
    tamoxifene = models.IntegerField(blank=True, null=True)
    bicalutamide = models.IntegerField(blank=True, null=True)
    cyproterone = models.IntegerField(blank=True, null=True)
    flutamide = models.IntegerField(blank=True, null=True)
    nilutamide = models.IntegerField(blank=True, null=True)
    lenalidomide = models.IntegerField(blank=True, null=True)
    pomalidomide = models.IntegerField(blank=True, null=True)
    thalidomide = models.IntegerField(blank=True, null=True)
    interferon = models.IntegerField(blank=True, null=True)
    anti_vegf = models.IntegerField(blank=True, null=True)
    iptk = models.IntegerField(blank=True, null=True)
    carflizomib = models.IntegerField(blank=True, null=True)
    bortezomib = models.IntegerField(blank=True, null=True)
    busulfan = models.IntegerField(blank=True, null=True)
    bleomycine = models.IntegerField(blank=True, null=True)
    corticoides = models.IntegerField(blank=True, null=True)
    autogreffe = models.IntegerField(blank=True, null=True)
    allogreffe = models.IntegerField(blank=True, null=True)
    anagrelide = models.IntegerField(blank=True, null=True)
    ruxolitinib = models.IntegerField(blank=True, null=True)
    urta = models.CharField(max_length=45, blank=True, null=True)
    catheter_veineux_centrale = models.CharField(max_length=45, blank=True, null=True)
    fac_ris_hem = models.CharField(max_length=45, blank=True, null=True)
    thro_dep_diag_can = models.CharField(max_length=45, blank=True, null=True)
    date_tddc = models.DateField(blank=True, null=True)
    tt_anti = models.CharField(max_length=45, blank=True, null=True)
    date_tta = models.DateField(blank=True, null=True)
    patient_idpatient = models.ForeignKey(Patient, models.DO_NOTHING, db_column='patient_idpatient')

    class Meta:
        managed = True
        db_table = 'traitement_ant'
        unique_together = (('id', 'patient_idpatient'),)


class TromboseArteriel(models.Model):
    idtrombose_arteriel = models.AutoField(primary_key=True)
    localisation = models.CharField(max_length=45, blank=True, null=True)
    date_diagnostic = models.DateField(blank=True, null=True)
    imagerie_diagnostique = models.CharField(max_length=45, blank=True, null=True)
    changement_traitemnt = models.CharField(max_length=45, blank=True, null=True) #
    traitemnt_precedent = models.CharField(max_length=45, blank=True, null=True) #
    dose_prec = models.FloatField(blank=True, null=True) #
    traitement_antithrombotique = models.CharField(max_length=45, blank=True, null=True)
    dose = models.FloatField(blank=True, null=True)
    date_init_traitement = models.DateField(blank=True, null=True)
    duree_traitement = models.IntegerField(blank=True, null=True)

    recidive = models.IntegerField(blank=True, null=True)
    recdtat_date = models.DateField(blank=True, null=True)
    recdtat_type = models.CharField(max_length=45, blank=True, null=True)
    recdtat_localisation = models.CharField(max_length=10000, blank=True, null=True)
    hemoragie = models.IntegerField(blank=True, null=True)
    date_hemor = models.DateField(blank=True, null=True)
    charactere_hemor = models.CharField(max_length=45, blank=True, null=True)

    patient_idpatient = models.ForeignKey(Patient, models.DO_NOTHING, db_column='patient_idpatient')

    class Meta:
        managed = True
        db_table = 'trombose_arteriel'
        unique_together = (('idtrombose_arteriel', 'patient_idpatient'),)


class TromboseRecidivant(models.Model):
    idtrombose_recidivant = models.AutoField(primary_key=True)
    aucun = models.IntegerField(blank=True, null=True)
    tamt_arret_depuis = models.IntegerField(blank=True, null=True)
    antiagregants_plaq = models.CharField(max_length=20, blank=True, null=True)
    dernier_val_antxa = models.IntegerField(blank=True, null=True)
    date_dva = models.DateField(blank=True, null=True)
    heparine = models.IntegerField(blank=True, null=True)
    avk = models.IntegerField(blank=True, null=True)
    dernier_inr = models.CharField(max_length=45, blank=True, null=True)
    date_di = models.DateField(blank=True, null=True)
    aod = models.IntegerField(blank=True, null=True)
    comp_trait = models.IntegerField(blank=True, null=True)
    patient_idpatient = models.ForeignKey(Patient, models.DO_NOTHING, db_column='patient_idpatient')

    class Meta:
        managed = True
        db_table = 'trombose_recidivant'
        unique_together = (('idtrombose_recidivant', 'patient_idpatient'),)


class TromboseVeineuse(models.Model):
    idtrombose_veineuse = models.AutoField(primary_key=True)
    localisation = models.CharField(max_length=45, blank=True, null=True)
    date_diagnostique = models.DateField(blank=True, null=True)
    conditions = models.CharField(max_length=45, blank=True, null=True)
    #facteur declanchant
    fc_ActivitePhysiqueIntense = models.IntegerField(blank=True, null=True)  # Activité physique intense
    fc_AlitementProlonge = models.IntegerField(blank=True, null=True)  # Alitement prolongé suite à une maladie
    fc_Cancer = models.IntegerField(blank=True, null=True)  # Cancer
    fc_ChirurgieAnesthésieGenerale = models.IntegerField(blank=True, null=True)  # Chirurgie sous anesthésie générale
    fc_Depression = models.IntegerField(blank=True, null=True)  # Dépression
    fc_Grossesse = models.IntegerField(blank=True, null=True)  # Grossesse
    fc_HospitalisationAffectionMedicaleAigue = models.IntegerField(blank=True, null=True)  # Hospitalisation pour une affection médicale aiguë
    fc_ImmobilisationPlatre = models.IntegerField(blank=True, null=True)  # Immobilisation sous plâtre
    fc_StressPsychologiqueIntense = models.IntegerField(blank=True, null=True)  # Stress psychologique intense
    fc_VoyageAvion = models.IntegerField(blank=True, null=True)  # Voyage en avion > 4 heures
    fc_VoyageVoiture = models.IntegerField(blank=True, null=True)  # Voyage en voiture > 6 heures
    fc_pellule_oestroprogestatif = models.IntegerField(blank=True, null=True)
    fc_traitement_hormonal_substituf = models.IntegerField(blank=True, null=True)


    imagerie_diagnostique = models.CharField(max_length=45, blank=True, null=True)
    changement_traitemnt = models.CharField(max_length=45, blank=True, null=True) #
    traitemnt_precedent = models.CharField(max_length=45, blank=True, null=True) #
    dose_prec = models.FloatField(blank=True, null=True) #
    traitement_antithrombotique = models.CharField(max_length=45, blank=True, null=True)
    dose = models.FloatField(blank=True, null=True)
    date_init_traitement = models.DateField(blank=True, null=True)
    duree_traitement = models.IntegerField(blank=True, null=True)
    recidive = models.IntegerField(blank=True, null=True)
    recdtat_date = models.DateField(blank=True, null=True)
    recdtat_type = models.CharField(max_length=45, blank=True, null=True)
    recdtat_localisation = models.CharField(max_length=10000, blank=True, null=True)
    hemoragie = models.IntegerField(blank=True, null=True)
    date_hemor = models.DateField(blank=True, null=True)
    charactere_hemor = models.CharField(max_length=45, blank=True, null=True)
    local_hemor = models.TextField(blank=True, null=True)
    patient_idpatient = models.ForeignKey(Patient, models.DO_NOTHING, db_column='patient_idpatient')

    class Meta:
        managed = True
        db_table = 'trombose_veineuse'
        unique_together = (('idtrombose_veineuse', 'patient_idpatient'),)


class VillaltaSyndrome(models.Model):
    idvillalta_syndrome = models.AutoField(primary_key=True)
    pain = models.IntegerField(blank=True, null=True)
    cramps = models.IntegerField(blank=True, null=True)
    heaviness = models.IntegerField(blank=True, null=True)
    paresthesia = models.IntegerField(blank=True, null=True)
    pruritus = models.IntegerField(blank=True, null=True)
    pretibial_edema = models.IntegerField(blank=True, null=True)
    skin_induration = models.IntegerField(blank=True, null=True)
    hyperpigmentation = models.IntegerField(blank=True, null=True)
    redness = models.IntegerField(blank=True, null=True)
    venous_ectasia = models.IntegerField(blank=True, null=True)
    pain_calf_com = models.IntegerField(blank=True, null=True)
    venous_ulcers = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    patient_idpatient = models.ForeignKey(Patient, models.DO_NOTHING, db_column='patient_idpatient')

    class Meta:
        managed = True
        db_table = 'villalta_syndrome'
        unique_together = (('idvillalta_syndrome', 'patient_idpatient'),)

class MyelomeMultiple(models.Model):
    idmyelome_multiple = models.AutoField(primary_key=True)
    type_ig = models.CharField(max_length=45,blank=True,null=True)
    chaine_legere = models.CharField(max_length=45,blank=True,null=True)
    stade_salmon = models.IntegerField(blank=True,null=True)
    iss = models.IntegerField(blank=True, null=True)
    stade_evolutif = models.CharField(max_length=40,null=True)
    temp_ecoule = models.CharField(max_length=45, blank=True, null=True)
    score_ecog = models.IntegerField(blank=True, null=True)
    indice_perf_ocog = models.CharField(max_length=45, blank=True, null=True)
    pathologie_malaincol = models.CharField(max_length=45, blank=True, null=True)
    patient_idpatient = models.ForeignKey('Patient', models.DO_NOTHING, db_column='patient_idpatient')

    class Meta:
        managed = True
        db_table = 'myelome_multiple'
        unique_together = (('idmyelome_multiple', 'patient_idpatient'),)



