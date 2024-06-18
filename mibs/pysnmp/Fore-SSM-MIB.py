#
# PySNMP MIB module Fore-SSM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Fore-SSM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:03:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
syncStatusMsgGroup, = mibBuilder.importSymbols("Fore-Switch-MIB", "syncStatusMsgGroup")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Counter64, MibIdentifier, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Gauge32, Integer32, NotificationType, TimeTicks, Counter32, Bits, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter64", "MibIdentifier", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Gauge32", "Integer32", "NotificationType", "TimeTicks", "Counter32", "Bits", "ModuleIdentity", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sysStatusMsgModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 21, 4))
if mibBuilder.loadTexts: sysStatusMsgModule.setLastUpdated('9912090000Z')
if mibBuilder.loadTexts: sysStatusMsgModule.setOrganization('FORE')
class SyncStatusMsgType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 13, 15, 16, 100, 101))
    namedValues = NamedValues(("prs", 1), ("prc", 2), ("stu", 3), ("st2", 4), ("tncssua", 5), ("st3e", 8), ("ssub", 9), ("st3", 10), ("sec", 11), ("smc", 12), ("st4", 13), ("res", 15), ("dus", 16), ("invalid", 100), ("none", 101))

syncStatusMsgTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 21, 1), )
if mibBuilder.loadTexts: syncStatusMsgTable.setStatus('current')
syncStatusMsgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 21, 1, 1), ).setIndexNames((1, "Fore-SSM-MIB", "syncStatusMsgInterface"))
if mibBuilder.loadTexts: syncStatusMsgEntry.setStatus('current')
syncStatusMsgInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 21, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255)))
if mibBuilder.loadTexts: syncStatusMsgInterface.setStatus('current')
syncStatusMsgRxMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 21, 1, 1, 2), SyncStatusMsgType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syncStatusMsgRxMessage.setStatus('current')
syncStatusMsgTxMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 21, 1, 1, 3), SyncStatusMsgType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syncStatusMsgTxMessage.setStatus('current')
syncStatusMsgForceRxSsm = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 21, 1, 1, 4), SyncStatusMsgType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syncStatusMsgForceRxSsm.setStatus('current')
syncStatusMsgForceDus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 21, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syncStatusMsgForceDus.setStatus('current')
syncStatusMsgPrevRxMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 21, 1, 1, 6), SyncStatusMsgType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: syncStatusMsgPrevRxMessage.setStatus('current')
syncStatusMsgAutomaticRefSwitching = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 21, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syncStatusMsgAutomaticRefSwitching.setStatus('current')
syncStatusMsgSdhOption = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 21, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("optionI", 1), ("optionII", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syncStatusMsgSdhOption.setStatus('current')
syncStatusMsgChanged = NotificationType((1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 21, 0, 1)).setObjects(("Fore-SSM-MIB", "syncStatusMsgPrevRxMessage"), ("Fore-SSM-MIB", "syncStatusMsgRxMessage"))
if mibBuilder.loadTexts: syncStatusMsgChanged.setStatus('current')
mibBuilder.exportSymbols("Fore-SSM-MIB", sysStatusMsgModule=sysStatusMsgModule, syncStatusMsgInterface=syncStatusMsgInterface, PYSNMP_MODULE_ID=sysStatusMsgModule, syncStatusMsgSdhOption=syncStatusMsgSdhOption, syncStatusMsgPrevRxMessage=syncStatusMsgPrevRxMessage, syncStatusMsgAutomaticRefSwitching=syncStatusMsgAutomaticRefSwitching, syncStatusMsgChanged=syncStatusMsgChanged, SyncStatusMsgType=SyncStatusMsgType, syncStatusMsgTxMessage=syncStatusMsgTxMessage, syncStatusMsgForceDus=syncStatusMsgForceDus, syncStatusMsgForceRxSsm=syncStatusMsgForceRxSsm, syncStatusMsgTable=syncStatusMsgTable, syncStatusMsgEntry=syncStatusMsgEntry, syncStatusMsgRxMessage=syncStatusMsgRxMessage)
