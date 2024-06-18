#
# PySNMP MIB module ASCEND-MIBLOADSELECT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBLOADSELECT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:11:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Integer32, Bits, ModuleIdentity, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, Counter32, Unsigned32, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "Bits", "ModuleIdentity", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "IpAddress", "Counter32", "Unsigned32", "iso", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibloadSelectProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 92))
mibloadSelectProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 92, 1), )
if mibBuilder.loadTexts: mibloadSelectProfileTable.setStatus('mandatory')
mibloadSelectProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1), ).setIndexNames((0, "ASCEND-MIBLOADSELECT-MIB", "loadSelectProfile-Index-o"))
if mibBuilder.loadTexts: mibloadSelectProfileEntry.setStatus('mandatory')
loadSelectProfile_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 1), Integer32()).setLabel("loadSelectProfile-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: loadSelectProfile_Index_o.setStatus('mandatory')
loadSelectProfile_UnknownCards = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-UnknownCards").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_UnknownCards.setStatus('mandatory')
loadSelectProfile_Sr = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Sr").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Sr.setStatus('mandatory')
loadSelectProfile_Sr2 = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Sr2").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Sr2.setStatus('mandatory')
loadSelectProfile_Apxsr = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Apxsr").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Apxsr.setStatus('mandatory')
loadSelectProfile_o8t1 = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-o8t1").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_o8t1.setStatus('mandatory')
loadSelectProfile_o8e1 = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-o8e1").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_o8e1.setStatus('mandatory')
loadSelectProfile_T3 = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-T3").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_T3.setStatus('mandatory')
loadSelectProfile_Stm0 = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Stm0").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Stm0.setStatus('mandatory')
loadSelectProfile_Pctfit = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Pctfit").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Pctfit.setStatus('mandatory')
loadSelectProfile_Pctfie = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Pctfie").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Pctfie.setStatus('mandatory')
loadSelectProfile_Clpmt = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Clpmt").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Clpmt.setStatus('mandatory')
loadSelectProfile_Clpme = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Clpme").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Clpme.setStatus('mandatory')
loadSelectProfile_o24t1 = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 64), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-o24t1").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_o24t1.setStatus('mandatory')
loadSelectProfile_o24e1 = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 65), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-o24e1").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_o24e1.setStatus('mandatory')
loadSelectProfile_Cln = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 72), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Cln").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Cln.setStatus('mandatory')
loadSelectProfile_Alpmt = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 75), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Alpmt").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Alpmt.setStatus('mandatory')
loadSelectProfile_Alpme = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 76), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Alpme").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Alpme.setStatus('mandatory')
loadSelectProfile_Ut1 = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Ut1").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Ut1.setStatus('mandatory')
loadSelectProfile_Ue1 = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Ue1").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Ue1.setStatus('mandatory')
loadSelectProfile_Uds3 = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Uds3").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Uds3.setStatus('mandatory')
loadSelectProfile_Ds3Atm = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Ds3Atm").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Ds3Atm.setStatus('mandatory')
loadSelectProfile_AtmHse = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 68), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-AtmHse").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_AtmHse.setStatus('mandatory')
loadSelectProfile_Enet2 = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Enet2").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Enet2.setStatus('mandatory')
loadSelectProfile_Enet3 = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Enet3").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Enet3.setStatus('mandatory')
loadSelectProfile_Enet3nd = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Enet3nd").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Enet3nd.setStatus('mandatory')
loadSelectProfile_EtherDual = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-EtherDual").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_EtherDual.setStatus('mandatory')
loadSelectProfile_SrsEther = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-SrsEther").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_SrsEther.setStatus('mandatory')
loadSelectProfile_EnetHse = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 69), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-EnetHse").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_EnetHse.setStatus('mandatory')
loadSelectProfile_Apxenet = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 82), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Apxenet").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Apxenet.setStatus('mandatory')
loadSelectProfile_MdmV34 = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-MdmV34").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_MdmV34.setStatus('mandatory')
loadSelectProfile_Mdm56k = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Mdm56k").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Mdm56k.setStatus('mandatory')
loadSelectProfile_Amdm = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Amdm").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Amdm.setStatus('mandatory')
loadSelectProfile_Anmdm = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Anmdm").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Anmdm.setStatus('mandatory')
loadSelectProfile_Csmx = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 28), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Csmx").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Csmx.setStatus('mandatory')
loadSelectProfile_Madd = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 29), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Madd").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Madd.setStatus('mandatory')
loadSelectProfile_Csm3v = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 30), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Csm3v").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Csm3v.setStatus('mandatory')
loadSelectProfile_Madd3 = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 31), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Madd3").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Madd3.setStatus('mandatory')
loadSelectProfile_Hdlc2 = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 33), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Hdlc2").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Hdlc2.setStatus('mandatory')
loadSelectProfile_Hdlc2ec = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 34), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Hdlc2ec").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Hdlc2ec.setStatus('mandatory')
loadSelectProfile_Swan = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 35), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Swan").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Swan.setStatus('mandatory')
loadSelectProfile_Hssi = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 36), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Hssi").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Hssi.setStatus('mandatory')
loadSelectProfile_Idsl = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 37), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Idsl").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Idsl.setStatus('mandatory')
loadSelectProfile_Capadsl = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 38), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Capadsl").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Capadsl.setStatus('mandatory')
loadSelectProfile_Dmtadsl = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 39), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Dmtadsl").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Dmtadsl.setStatus('mandatory')
loadSelectProfile_Sdsl = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 40), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Sdsl").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Sdsl.setStatus('mandatory')
loadSelectProfile_Sdsl70d = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 41), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Sdsl70d").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Sdsl70d.setStatus('mandatory')
loadSelectProfile_Sdsl70v = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 42), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Sdsl70v").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Sdsl70v.setStatus('mandatory')
loadSelectProfile_Oc3Atm = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 43), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Oc3Atm").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Oc3Atm.setStatus('mandatory')
loadSelectProfile_SdslAtm = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 44), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-SdslAtm").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_SdslAtm.setStatus('mandatory')
loadSelectProfile_AlDmtadslAtm = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 45), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-AlDmtadslAtm").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_AlDmtadslAtm.setStatus('mandatory')
loadSelectProfile_SdslAtmV2 = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 46), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-SdslAtmV2").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_SdslAtmV2.setStatus('mandatory')
loadSelectProfile_DadslAtm24 = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 47), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-DadslAtm24").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_DadslAtm24.setStatus('mandatory')
loadSelectProfile_GliteAtm48 = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 48), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-GliteAtm48").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_GliteAtm48.setStatus('mandatory')
loadSelectProfile_Hdsl2 = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 49), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Hdsl2").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Hdsl2.setStatus('mandatory')
loadSelectProfile_AnnexbDmtadsl = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 50), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-AnnexbDmtadsl").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_AnnexbDmtadsl.setStatus('mandatory')
loadSelectProfile_T1000 = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 51), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-T1000").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_T1000.setStatus('mandatory')
loadSelectProfile_Ima = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 52), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Ima").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Ima.setStatus('mandatory')
loadSelectProfile_Stngr32Idsl = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 53), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Stngr32Idsl").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Stngr32Idsl.setStatus('mandatory')
loadSelectProfile_o40DmtAdsl = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 54), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-o40DmtAdsl").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_o40DmtAdsl.setStatus('mandatory')
loadSelectProfile_o48DmtAdsl = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 55), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-o48DmtAdsl").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_o48DmtAdsl.setStatus('mandatory')
loadSelectProfile_o72Shdsl = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 62), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-o72Shdsl").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_o72Shdsl.setStatus('mandatory')
loadSelectProfile_o72CtDmtAdsl = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 77), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-o72CtDmtAdsl").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_o72CtDmtAdsl.setStatus('mandatory')
loadSelectProfile_o32DmtAslam = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 70), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-o32DmtAslam").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_o32DmtAslam.setStatus('mandatory')
loadSelectProfile_Vdsl = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 71), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Vdsl").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Vdsl.setStatus('mandatory')
loadSelectProfile_Ds3Atm2 = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 56), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Ds3Atm2").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Ds3Atm2.setStatus('mandatory')
loadSelectProfile_E3Atm = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 57), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-E3Atm").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_E3Atm.setStatus('mandatory')
loadSelectProfile_Oc3Atm2 = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 58), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Oc3Atm2").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Oc3Atm2.setStatus('mandatory')
loadSelectProfile_Vpn = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 59), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Vpn").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Vpn.setStatus('mandatory')
loadSelectProfile_Swan2 = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 60), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("load", 2), ("skip", 3)))).setLabel("loadSelectProfile-Swan2").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Swan2.setStatus('mandatory')
loadSelectProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 92, 1, 1, 61), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("loadSelectProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadSelectProfile_Action_o.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBLOADSELECT-MIB", loadSelectProfile_Vpn=loadSelectProfile_Vpn, loadSelectProfile_Stm0=loadSelectProfile_Stm0, loadSelectProfile_Dmtadsl=loadSelectProfile_Dmtadsl, loadSelectProfile_Ut1=loadSelectProfile_Ut1, loadSelectProfile_Clpmt=loadSelectProfile_Clpmt, loadSelectProfile_o24t1=loadSelectProfile_o24t1, loadSelectProfile_Alpme=loadSelectProfile_Alpme, loadSelectProfile_o8e1=loadSelectProfile_o8e1, loadSelectProfile_Enet2=loadSelectProfile_Enet2, loadSelectProfile_Hdlc2=loadSelectProfile_Hdlc2, mibloadSelectProfileTable=mibloadSelectProfileTable, loadSelectProfile_Ue1=loadSelectProfile_Ue1, loadSelectProfile_Ds3Atm=loadSelectProfile_Ds3Atm, loadSelectProfile_Idsl=loadSelectProfile_Idsl, loadSelectProfile_Stngr32Idsl=loadSelectProfile_Stngr32Idsl, loadSelectProfile_Csmx=loadSelectProfile_Csmx, loadSelectProfile_o48DmtAdsl=loadSelectProfile_o48DmtAdsl, loadSelectProfile_Enet3nd=loadSelectProfile_Enet3nd, loadSelectProfile_E3Atm=loadSelectProfile_E3Atm, loadSelectProfile_Anmdm=loadSelectProfile_Anmdm, loadSelectProfile_Madd=loadSelectProfile_Madd, loadSelectProfile_Swan2=loadSelectProfile_Swan2, loadSelectProfile_SrsEther=loadSelectProfile_SrsEther, loadSelectProfile_Sdsl70v=loadSelectProfile_Sdsl70v, loadSelectProfile_Action_o=loadSelectProfile_Action_o, loadSelectProfile_Enet3=loadSelectProfile_Enet3, loadSelectProfile_T3=loadSelectProfile_T3, loadSelectProfile_Csm3v=loadSelectProfile_Csm3v, loadSelectProfile_Alpmt=loadSelectProfile_Alpmt, loadSelectProfile_EnetHse=loadSelectProfile_EnetHse, loadSelectProfile_UnknownCards=loadSelectProfile_UnknownCards, loadSelectProfile_o8t1=loadSelectProfile_o8t1, loadSelectProfile_SdslAtmV2=loadSelectProfile_SdslAtmV2, loadSelectProfile_Ima=loadSelectProfile_Ima, loadSelectProfile_Mdm56k=loadSelectProfile_Mdm56k, loadSelectProfile_MdmV34=loadSelectProfile_MdmV34, loadSelectProfile_Clpme=loadSelectProfile_Clpme, loadSelectProfile_Apxenet=loadSelectProfile_Apxenet, loadSelectProfile_o40DmtAdsl=loadSelectProfile_o40DmtAdsl, loadSelectProfile_Sr=loadSelectProfile_Sr, loadSelectProfile_Cln=loadSelectProfile_Cln, loadSelectProfile_Vdsl=loadSelectProfile_Vdsl, mibloadSelectProfile=mibloadSelectProfile, loadSelectProfile_T1000=loadSelectProfile_T1000, loadSelectProfile_o32DmtAslam=loadSelectProfile_o32DmtAslam, loadSelectProfile_Hdlc2ec=loadSelectProfile_Hdlc2ec, loadSelectProfile_Ds3Atm2=loadSelectProfile_Ds3Atm2, loadSelectProfile_Sr2=loadSelectProfile_Sr2, loadSelectProfile_Madd3=loadSelectProfile_Madd3, loadSelectProfile_Pctfie=loadSelectProfile_Pctfie, loadSelectProfile_Swan=loadSelectProfile_Swan, loadSelectProfile_Hssi=loadSelectProfile_Hssi, loadSelectProfile_Sdsl=loadSelectProfile_Sdsl, loadSelectProfile_Pctfit=loadSelectProfile_Pctfit, loadSelectProfile_Oc3Atm=loadSelectProfile_Oc3Atm, loadSelectProfile_AnnexbDmtadsl=loadSelectProfile_AnnexbDmtadsl, DisplayString=DisplayString, loadSelectProfile_Uds3=loadSelectProfile_Uds3, loadSelectProfile_o72CtDmtAdsl=loadSelectProfile_o72CtDmtAdsl, loadSelectProfile_SdslAtm=loadSelectProfile_SdslAtm, loadSelectProfile_GliteAtm48=loadSelectProfile_GliteAtm48, loadSelectProfile_Capadsl=loadSelectProfile_Capadsl, loadSelectProfile_Oc3Atm2=loadSelectProfile_Oc3Atm2, loadSelectProfile_o24e1=loadSelectProfile_o24e1, loadSelectProfile_AlDmtadslAtm=loadSelectProfile_AlDmtadslAtm, loadSelectProfile_EtherDual=loadSelectProfile_EtherDual, loadSelectProfile_Hdsl2=loadSelectProfile_Hdsl2, loadSelectProfile_Sdsl70d=loadSelectProfile_Sdsl70d, loadSelectProfile_o72Shdsl=loadSelectProfile_o72Shdsl, loadSelectProfile_Index_o=loadSelectProfile_Index_o, mibloadSelectProfileEntry=mibloadSelectProfileEntry, loadSelectProfile_DadslAtm24=loadSelectProfile_DadslAtm24, loadSelectProfile_Amdm=loadSelectProfile_Amdm, loadSelectProfile_AtmHse=loadSelectProfile_AtmHse, loadSelectProfile_Apxsr=loadSelectProfile_Apxsr)
