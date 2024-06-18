#
# PySNMP MIB module HH3C-FR-QOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-FR-QOS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:14:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
hh3cQoS, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cQoS")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, Counter64, ModuleIdentity, iso, IpAddress, TimeTicks, Unsigned32, Gauge32, ObjectIdentity, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "Counter64", "ModuleIdentity", "iso", "IpAddress", "TimeTicks", "Unsigned32", "Gauge32", "ObjectIdentity", "Counter32", "Bits")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
hh3cFrQoSMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3))
if mibBuilder.loadTexts: hh3cFrQoSMib.setLastUpdated('200407120000Z')
if mibBuilder.loadTexts: hh3cFrQoSMib.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
class Hh3cCirAllowDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("inbound", 1), ("outbound", 2), ("inboundAndOutbound", 3))

hh3cFrQoSObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1))
hh3cFrClassObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1))
hh3cFrClassIndexNext = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFrClassIndexNext.setStatus('current')
hh3cFrClassCfgInfoTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 2), )
if mibBuilder.loadTexts: hh3cFrClassCfgInfoTable.setStatus('current')
hh3cFrClassCfgInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 2, 1), ).setIndexNames((0, "HH3C-FR-QOS-MIB", "hh3cFrClassIndex"))
if mibBuilder.loadTexts: hh3cFrClassCfgInfoEntry.setStatus('current')
hh3cFrClassIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: hh3cFrClassIndex.setStatus('current')
hh3cFrClassName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFrClassName.setStatus('current')
hh3cFrClassRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFrClassRowStatus.setStatus('current')
hh3cCirAllowCfgInfoTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 3), )
if mibBuilder.loadTexts: hh3cCirAllowCfgInfoTable.setStatus('current')
hh3cCirAllowCfgInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 3, 1), ).setIndexNames((0, "HH3C-FR-QOS-MIB", "hh3cCirAllowFrClassIndex"), (0, "HH3C-FR-QOS-MIB", "hh3cCirAllowDirection"))
if mibBuilder.loadTexts: hh3cCirAllowCfgInfoEntry.setStatus('current')
hh3cCirAllowFrClassIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: hh3cCirAllowFrClassIndex.setStatus('current')
hh3cCirAllowDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 3, 1, 2), Hh3cCirAllowDirection())
if mibBuilder.loadTexts: hh3cCirAllowDirection.setStatus('current')
hh3cCirAllowValue = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 45000000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cCirAllowValue.setStatus('current')
hh3cCirAllowRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cCirAllowRowStatus.setStatus('current')
hh3cCirCfgInfoTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 4), )
if mibBuilder.loadTexts: hh3cCirCfgInfoTable.setStatus('current')
hh3cCirCfgInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 4, 1), ).setIndexNames((0, "HH3C-FR-QOS-MIB", "hh3cCirFrClassIndex"))
if mibBuilder.loadTexts: hh3cCirCfgInfoEntry.setStatus('current')
hh3cCirFrClassIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 4, 1, 1), Integer32())
if mibBuilder.loadTexts: hh3cCirFrClassIndex.setStatus('current')
hh3cCirValue = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1000, 45000000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cCirValue.setStatus('current')
hh3cCirRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 4, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cCirRowStatus.setStatus('current')
hh3cIfApplyFrClassTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 5), )
if mibBuilder.loadTexts: hh3cIfApplyFrClassTable.setStatus('current')
hh3cIfApplyFrClassEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 5, 1), ).setIndexNames((0, "HH3C-FR-QOS-MIB", "hh3cIfApplyFrClassIfIndex"))
if mibBuilder.loadTexts: hh3cIfApplyFrClassEntry.setStatus('current')
hh3cIfApplyFrClassIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 5, 1, 1), Integer32())
if mibBuilder.loadTexts: hh3cIfApplyFrClassIfIndex.setStatus('current')
hh3cIfApplyFrClassIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 5, 1, 2), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cIfApplyFrClassIndex.setStatus('current')
hh3cIfApplyFrClassRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 5, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cIfApplyFrClassRowStatus.setStatus('current')
hh3cPvcApplyFrClassTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 6), )
if mibBuilder.loadTexts: hh3cPvcApplyFrClassTable.setStatus('current')
hh3cPvcApplyFrClassEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 6, 1), ).setIndexNames((0, "HH3C-FR-QOS-MIB", "hh3cPvcApplyFrClassIfIndex"), (0, "HH3C-FR-QOS-MIB", "hh3cPvcApplyFrClassDlciNum"))
if mibBuilder.loadTexts: hh3cPvcApplyFrClassEntry.setStatus('current')
hh3cPvcApplyFrClassIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 6, 1, 1), Integer32())
if mibBuilder.loadTexts: hh3cPvcApplyFrClassIfIndex.setStatus('current')
hh3cPvcApplyFrClassDlciNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(16, 1007)))
if mibBuilder.loadTexts: hh3cPvcApplyFrClassDlciNum.setStatus('current')
hh3cPvcApplyFrClassIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 6, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPvcApplyFrClassIndex.setStatus('current')
hh3cPvcApplyFrClassRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 6, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPvcApplyFrClassRowStatus.setStatus('current')
hh3cFrPvcBandwidthTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 7), )
if mibBuilder.loadTexts: hh3cFrPvcBandwidthTable.setStatus('current')
hh3cFrPvcBandwidthEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 7, 1), ).setIndexNames((0, "HH3C-FR-QOS-MIB", "hh3cPvcApplyFrClassIfIndex"), (0, "HH3C-FR-QOS-MIB", "hh3cPvcApplyFrClassDlciNum"))
if mibBuilder.loadTexts: hh3cFrPvcBandwidthEntry.setStatus('current')
hh3cFrPvcBandwidthMaxReservedBW = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 7, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFrPvcBandwidthMaxReservedBW.setStatus('current')
hh3cFrPvcBandwidthAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 1, 7, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFrPvcBandwidthAvailable.setStatus('current')
hh3cRTPQoSObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 2))
hh3cRTPFrClassApplyTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 2, 1), )
if mibBuilder.loadTexts: hh3cRTPFrClassApplyTable.setStatus('current')
hh3cRTPFrClassApplyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 2, 1, 1), ).setIndexNames((0, "HH3C-FR-QOS-MIB", "hh3cRTPFrClassApplyFrClassIndex"))
if mibBuilder.loadTexts: hh3cRTPFrClassApplyEntry.setStatus('current')
hh3cRTPFrClassApplyFrClassIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 2, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: hh3cRTPFrClassApplyFrClassIndex.setStatus('current')
hh3cRTPFrClassApplyStartPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2000, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cRTPFrClassApplyStartPort.setStatus('current')
hh3cRTPFrClassApplyEndPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2000, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cRTPFrClassApplyEndPort.setStatus('current')
hh3cRTPFrClassApplyBandWidth = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(8, 1000000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cRTPFrClassApplyBandWidth.setStatus('current')
hh3cRTPFrClassApplyCbs = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1500, 2000000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cRTPFrClassApplyCbs.setStatus('current')
hh3cRTPFrClassApplyRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 2, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cRTPFrClassApplyRowStatus.setStatus('current')
hh3cRTPFrPvcQueueRunInfoTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 2, 2), )
if mibBuilder.loadTexts: hh3cRTPFrPvcQueueRunInfoTable.setStatus('current')
hh3cRTPFrPvcQueueRunInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 2, 2, 1), ).setIndexNames((0, "HH3C-FR-QOS-MIB", "hh3cPvcApplyFrClassIfIndex"), (0, "HH3C-FR-QOS-MIB", "hh3cPvcApplyFrClassDlciNum"))
if mibBuilder.loadTexts: hh3cRTPFrPvcQueueRunInfoEntry.setStatus('current')
hh3cRTPFrPvcQueueSize = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRTPFrPvcQueueSize.setStatus('current')
hh3cRTPFrPvcQueueMaxSize = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRTPFrPvcQueueMaxSize.setStatus('current')
hh3cRTPFrPvcQueueOutputs = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 2, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRTPFrPvcQueueOutputs.setStatus('current')
hh3cRTPFrPvcQueueDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 32, 3, 1, 2, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRTPFrPvcQueueDiscards.setStatus('current')
mibBuilder.exportSymbols("HH3C-FR-QOS-MIB", hh3cFrPvcBandwidthTable=hh3cFrPvcBandwidthTable, hh3cCirCfgInfoEntry=hh3cCirCfgInfoEntry, hh3cPvcApplyFrClassIndex=hh3cPvcApplyFrClassIndex, hh3cRTPFrClassApplyStartPort=hh3cRTPFrClassApplyStartPort, hh3cPvcApplyFrClassIfIndex=hh3cPvcApplyFrClassIfIndex, hh3cIfApplyFrClassTable=hh3cIfApplyFrClassTable, hh3cIfApplyFrClassEntry=hh3cIfApplyFrClassEntry, hh3cCirAllowRowStatus=hh3cCirAllowRowStatus, hh3cIfApplyFrClassIfIndex=hh3cIfApplyFrClassIfIndex, hh3cRTPFrClassApplyEndPort=hh3cRTPFrClassApplyEndPort, hh3cRTPFrPvcQueueOutputs=hh3cRTPFrPvcQueueOutputs, hh3cFrClassIndexNext=hh3cFrClassIndexNext, hh3cCirRowStatus=hh3cCirRowStatus, hh3cRTPFrClassApplyBandWidth=hh3cRTPFrClassApplyBandWidth, hh3cFrQoSMib=hh3cFrQoSMib, hh3cFrPvcBandwidthEntry=hh3cFrPvcBandwidthEntry, hh3cCirAllowFrClassIndex=hh3cCirAllowFrClassIndex, hh3cCirAllowDirection=hh3cCirAllowDirection, hh3cCirValue=hh3cCirValue, hh3cFrClassObjects=hh3cFrClassObjects, hh3cFrClassCfgInfoEntry=hh3cFrClassCfgInfoEntry, hh3cCirAllowCfgInfoTable=hh3cCirAllowCfgInfoTable, hh3cFrQoSObjects=hh3cFrQoSObjects, hh3cFrPvcBandwidthAvailable=hh3cFrPvcBandwidthAvailable, hh3cRTPFrClassApplyEntry=hh3cRTPFrClassApplyEntry, hh3cCirAllowCfgInfoEntry=hh3cCirAllowCfgInfoEntry, hh3cCirCfgInfoTable=hh3cCirCfgInfoTable, PYSNMP_MODULE_ID=hh3cFrQoSMib, hh3cRTPFrClassApplyCbs=hh3cRTPFrClassApplyCbs, hh3cFrClassRowStatus=hh3cFrClassRowStatus, hh3cPvcApplyFrClassTable=hh3cPvcApplyFrClassTable, hh3cRTPFrPvcQueueRunInfoEntry=hh3cRTPFrPvcQueueRunInfoEntry, hh3cRTPQoSObjects=hh3cRTPQoSObjects, hh3cFrClassCfgInfoTable=hh3cFrClassCfgInfoTable, hh3cCirFrClassIndex=hh3cCirFrClassIndex, hh3cRTPFrClassApplyRowStatus=hh3cRTPFrClassApplyRowStatus, hh3cPvcApplyFrClassDlciNum=hh3cPvcApplyFrClassDlciNum, hh3cIfApplyFrClassIndex=hh3cIfApplyFrClassIndex, hh3cRTPFrPvcQueueDiscards=hh3cRTPFrPvcQueueDiscards, hh3cFrClassIndex=hh3cFrClassIndex, hh3cRTPFrClassApplyFrClassIndex=hh3cRTPFrClassApplyFrClassIndex, hh3cRTPFrPvcQueueSize=hh3cRTPFrPvcQueueSize, hh3cRTPFrPvcQueueMaxSize=hh3cRTPFrPvcQueueMaxSize, hh3cPvcApplyFrClassRowStatus=hh3cPvcApplyFrClassRowStatus, hh3cFrPvcBandwidthMaxReservedBW=hh3cFrPvcBandwidthMaxReservedBW, Hh3cCirAllowDirection=Hh3cCirAllowDirection, hh3cFrClassName=hh3cFrClassName, hh3cRTPFrClassApplyTable=hh3cRTPFrClassApplyTable, hh3cPvcApplyFrClassEntry=hh3cPvcApplyFrClassEntry, hh3cRTPFrPvcQueueRunInfoTable=hh3cRTPFrPvcQueueRunInfoTable, hh3cCirAllowValue=hh3cCirAllowValue, hh3cIfApplyFrClassRowStatus=hh3cIfApplyFrClassRowStatus)
