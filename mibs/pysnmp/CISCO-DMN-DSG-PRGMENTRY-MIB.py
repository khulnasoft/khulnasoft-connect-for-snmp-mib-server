#
# PySNMP MIB module CISCO-DMN-DSG-PRGMENTRY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DMN-DSG-PRGMENTRY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:37:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, Counter32, Bits, MibIdentifier, Integer32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Unsigned32, ObjectIdentity, TimeTicks, Gauge32, IpAddress, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter32", "Bits", "MibIdentifier", "Integer32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Unsigned32", "ObjectIdentity", "TimeTicks", "Gauge32", "IpAddress", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoDSGProgramEntry = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4))
ciscoDSGProgramEntry.setRevisions(('2010-10-13 08:00', '2010-08-30 11:00', '2010-06-17 06:00', '2010-05-25 16:30', '2010-05-07 06:30', '2010-03-22 05:00', '2010-02-12 15:00', '2009-11-22 15:00',))
if mibBuilder.loadTexts: ciscoDSGProgramEntry.setLastUpdated('201010130800Z')
if mibBuilder.loadTexts: ciscoDSGProgramEntry.setOrganization('Cisco Systems, Inc.')
programEntryTable = MibIdentifier((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2))
programEntryControlTable = MibTable((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 1), )
if mibBuilder.loadTexts: programEntryControlTable.setStatus('current')
programEntryControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 1, 1), ).setIndexNames((0, "CISCO-DMN-DSG-PRGMENTRY-MIB", "programEntryControlIndex"))
if mibBuilder.loadTexts: programEntryControlEntry.setStatus('current')
programEntryControlIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32)))
if mibBuilder.loadTexts: programEntryControlIndex.setStatus('current')
programEntryControlChNum = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: programEntryControlChNum.setStatus('current')
programEntryControlChCmd = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("switch", 1), ("up", 2), ("down", 3), ("last", 4), ("writeOnly", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: programEntryControlChCmd.setStatus('current')
programEntryControlResourceId = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: programEntryControlResourceId.setStatus('current')
programEntryStatusTable = MibTable((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 2), )
if mibBuilder.loadTexts: programEntryStatusTable.setStatus('current')
programEntryStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 2, 1), ).setIndexNames((0, "CISCO-DMN-DSG-PRGMENTRY-MIB", "programEntryStatusIndex"))
if mibBuilder.loadTexts: programEntryStatusEntry.setStatus('current')
programEntryStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32)))
if mibBuilder.loadTexts: programEntryStatusIndex.setStatus('current')
programEntryStatusChName = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: programEntryStatusChName.setStatus('current')
programEntryStatusCAAuth = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: programEntryStatusCAAuth.setStatus('current')
programEntryStatusCAEncry = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("no", 1), ("yes", 2), ("unkn", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: programEntryStatusCAEncry.setStatus('current')
programEntryStatusCAScram = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: programEntryStatusCAScram.setStatus('current')
programEntryStatusCAID = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63))).clone(namedValues=NamedValues(("unknown", 1), ("fta", 2), ("powervu", 3), ("biss1", 4), ("biss2", 5), ("biss3", 6), ("standardized", 7), ("canalplus", 8), ("ccett", 9), ("deutscheTel", 10), ("eurodec", 11), ("franceTel", 12), ("iredeto", 13), ("jerroldGi", 14), ("matraComm", 15), ("nds", 16), ("nokia", 17), ("norwegianTel", 18), ("ntl", 19), ("philips", 20), ("sony", 21), ("tandbergTv", 22), ("thomson", 23), ("tvCom", 24), ("hptCroatian", 25), ("hrtCroatian", 26), ("ibm", 27), ("nera", 28), ("betaTechnik", 29), ("kudelski", 30), ("titanIS", 31), ("telefonica", 32), ("stentor", 33), ("tadiranScopus", 34), ("barco", 35), ("starguideDN", 36), ("mentorDS", 37), ("european", 38), ("polycipher", 39), ("generalIns", 40), ("telemann", 41), ("cryptoworks", 42), ("tsinghua", 43), ("easycas", 44), ("alphacrypt", 45), ("dvnHoldings", 46), ("shanghaiADT", 47), ("shenzhenKing", 48), ("sky", 49), ("dreamcrypt", 50), ("thalescrypt", 51), ("runcom", 52), ("sidsa", 53), ("beijingCom", 54), ("latens", 55), ("xcrypt", 56), ("beijingDig", 57), ("widevineTec", 58), ("skTel", 59), ("enigmaSys", 60), ("reserved", 61), ("ruscrypt", 62), ("other", 63)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: programEntryStatusCAID.setStatus('current')
programEntryStatusSRStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notStarted", 1), ("primary", 2), ("alternate", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: programEntryStatusSRStatus.setStatus('current')
programEntryStatusSRType = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("scheduled", 2), ("ca", 3), ("cuetrigger", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: programEntryStatusSRType.setStatus('current')
programEntryStatusSRStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 2, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: programEntryStatusSRStartTime.setStatus('current')
programEntryStatusSREndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 2, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: programEntryStatusSREndTime.setStatus('current')
programEntryStatusPRGMStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: programEntryStatusPRGMStatus.setStatus('current')
programEntryStatusPMTPID = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 2, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: programEntryStatusPMTPID.setStatus('current')
programEntryStatusPCRPID = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 2, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: programEntryStatusPCRPID.setStatus('current')
programEntryPIDTable = MibTable((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 3), )
if mibBuilder.loadTexts: programEntryPIDTable.setStatus('current')
programEntryPIDEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 3, 1), ).setIndexNames((0, "CISCO-DMN-DSG-PRGMENTRY-MIB", "programEntryPIDPEIndex"), (0, "CISCO-DMN-DSG-PRGMENTRY-MIB", "programEntryPIDIndex"))
if mibBuilder.loadTexts: programEntryPIDEntry.setStatus('current')
programEntryPIDPEIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 138)))
if mibBuilder.loadTexts: programEntryPIDPEIndex.setStatus('current')
programEntryPIDIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 138)))
if mibBuilder.loadTexts: programEntryPIDIndex.setStatus('current')
programEntryPIDTypeName = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: programEntryPIDTypeName.setStatus('current')
programEntryPIDTypeDetail = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42))).clone(namedValues=NamedValues(("pcr", 1), ("mpg1Vid", 2), ("mpg2Vid", 3), ("hdVid", 4), ("mpg4Vid", 5), ("iso422Vid", 6), ("h264Vid", 7), ("mpgAudL1", 8), ("mpg2AudL1", 9), ("mpgAudL2", 10), ("mpg2AudL2", 11), ("mpg4Aud", 12), ("dvbDolbyDigital", 13), ("dvbDolbyDigitalPlus", 14), ("atscDolbyDigital", 15), ("atscDolbyDigitalPlus", 16), ("aacLsAud", 17), ("haacLoAud", 18), ("haacAdAud", 19), ("dbeAud", 20), ("dtsAud", 21), ("dvbSubt", 22), ("saSubt", 23), ("dvbVbi", 24), ("saVbi", 25), ("dvbTtx", 26), ("scteDpi", 27), ("dvbMpe", 28), ("dvbAsyn", 29), ("dvbSyns", 30), ("dvbSynd", 31), ("dvbDcar", 32), ("dvbOcar", 33), ("saUtld", 34), ("saHsd", 35), ("saWbd", 36), ("saCddl", 37), ("ecm", 38), ("emm", 39), ("pmt", 40), ("unknown", 41), ("reserved", 42)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: programEntryPIDTypeDetail.setStatus('current')
programEntryPIDValue = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 3, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: programEntryPIDValue.setStatus('current')
programEntryPIDPresent = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 4, 2, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: programEntryPIDPresent.setStatus('current')
mibBuilder.exportSymbols("CISCO-DMN-DSG-PRGMENTRY-MIB", programEntryStatusPRGMStatus=programEntryStatusPRGMStatus, programEntryStatusSRStatus=programEntryStatusSRStatus, programEntryStatusIndex=programEntryStatusIndex, programEntryControlResourceId=programEntryControlResourceId, programEntryStatusChName=programEntryStatusChName, programEntryStatusCAScram=programEntryStatusCAScram, programEntryPIDPEIndex=programEntryPIDPEIndex, programEntryPIDTypeDetail=programEntryPIDTypeDetail, programEntryStatusSREndTime=programEntryStatusSREndTime, programEntryStatusTable=programEntryStatusTable, programEntryControlTable=programEntryControlTable, programEntryControlChCmd=programEntryControlChCmd, programEntryPIDTypeName=programEntryPIDTypeName, programEntryPIDPresent=programEntryPIDPresent, programEntryStatusPMTPID=programEntryStatusPMTPID, programEntryPIDTable=programEntryPIDTable, programEntryPIDValue=programEntryPIDValue, programEntryStatusSRStartTime=programEntryStatusSRStartTime, programEntryControlIndex=programEntryControlIndex, programEntryPIDEntry=programEntryPIDEntry, programEntryControlChNum=programEntryControlChNum, programEntryPIDIndex=programEntryPIDIndex, programEntryStatusCAID=programEntryStatusCAID, programEntryTable=programEntryTable, programEntryStatusCAAuth=programEntryStatusCAAuth, PYSNMP_MODULE_ID=ciscoDSGProgramEntry, programEntryStatusEntry=programEntryStatusEntry, ciscoDSGProgramEntry=ciscoDSGProgramEntry, programEntryControlEntry=programEntryControlEntry, programEntryStatusPCRPID=programEntryStatusPCRPID, programEntryStatusSRType=programEntryStatusSRType, programEntryStatusCAEncry=programEntryStatusCAEncry)
