#
# PySNMP MIB module Wellfleet-LNM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-LNM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:34:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Unsigned32, MibIdentifier, IpAddress, NotificationType, TimeTicks, ObjectIdentity, Counter32, Counter64, Bits, mib_2, iso, enterprises, NotificationType, Integer32, mgmt, Opaque, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Unsigned32", "MibIdentifier", "IpAddress", "NotificationType", "TimeTicks", "ObjectIdentity", "Counter32", "Counter64", "Bits", "mib-2", "iso", "enterprises", "NotificationType", "Integer32", "mgmt", "Opaque", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wfLanManagerGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfLanManagerGroup")
wfLnm = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 1))
wfLnmDelete = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfLnmDelete.setStatus('mandatory')
wfLnmDisable = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfLnmDisable.setStatus('mandatory')
wfLnmState = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("init", 3), ("notpresent", 4))).clone('down')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfLnmState.setStatus('mandatory')
wfLnmLnmSetsDisable = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfLnmLnmSetsDisable.setStatus('mandatory')
wfLnmInternalLanId = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfLnmInternalLanId.setStatus('mandatory')
wfLnmBridgeId = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfLnmBridgeId.setStatus('mandatory')
wfLnmInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2), )
if mibBuilder.loadTexts: wfLnmInterfaceTable.setStatus('mandatory')
wfLnmInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1), ).setIndexNames((0, "Wellfleet-LNM-MIB", "wfLnmInterfaceMacCircuit"))
if mibBuilder.loadTexts: wfLnmInterfaceEntry.setStatus('mandatory')
wfLnmInterfaceDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfLnmInterfaceDelete.setStatus('mandatory')
wfLnmInterfaceDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfLnmInterfaceDisable.setStatus('mandatory')
wfLnmInterfaceCircuit = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfLnmInterfaceCircuit.setStatus('mandatory')
wfLnmInterfaceMacCircuit = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfLnmInterfaceMacCircuit.setStatus('mandatory')
wfLnmInterfaceRemoteMac = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 5), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfLnmInterfaceRemoteMac.setStatus('mandatory')
wfLnmInterfaceLrmDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfLnmInterfaceLrmDisable.setStatus('mandatory')
wfLnmInterfaceLrmState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("init", 3), ("notpresent", 4))).clone('notpresent')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfLnmInterfaceLrmState.setStatus('mandatory')
wfLnmInterfaceLbsState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("init", 3), ("notpresent", 4))).clone('notpresent')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfLnmInterfaceLbsState.setStatus('mandatory')
wfLnmInterfaceRemDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfLnmInterfaceRemDisable.setStatus('mandatory')
wfLnmInterfaceRemState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("init", 3), ("notpresent", 4))).clone('notpresent')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfLnmInterfaceRemState.setStatus('mandatory')
wfLnmInterfaceRpsDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfLnmInterfaceRpsDisable.setStatus('mandatory')
wfLnmInterfaceRpsState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("init", 3), ("notpresent", 4))).clone('notpresent')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfLnmInterfaceRpsState.setStatus('mandatory')
wfLnmInterfaceCrsDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfLnmInterfaceCrsDisable.setStatus('mandatory')
wfLnmInterfaceCrsState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("init", 3), ("notpresent", 4))).clone('notpresent')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfLnmInterfaceCrsState.setStatus('mandatory')
wfLnmInterfaceCtrlMgrPswd = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 15), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfLnmInterfaceCtrlMgrPswd.setStatus('mandatory')
wfLnmInterfaceOb1MgrPswd = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 16), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfLnmInterfaceOb1MgrPswd.setStatus('mandatory')
wfLnmInterfaceOb2MgrPswd = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 17), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfLnmInterfaceOb2MgrPswd.setStatus('mandatory')
wfLnmInterfaceOb3MgrPswd = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 18), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfLnmInterfaceOb3MgrPswd.setStatus('mandatory')
wfLnmInterfaceCtrlMgrMac = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 19), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfLnmInterfaceCtrlMgrMac.setStatus('mandatory')
wfLnmInterfaceOb1MgrMac = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 20), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfLnmInterfaceOb1MgrMac.setStatus('mandatory')
wfLnmInterfaceOb2MgrMac = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 21), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfLnmInterfaceOb2MgrMac.setStatus('mandatory')
wfLnmInterfaceOb3MgrMac = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 22), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfLnmInterfaceOb3MgrMac.setStatus('mandatory')
wfLnmInterfaceWghtTrshld = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 256)).clone(128)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfLnmInterfaceWghtTrshld.setStatus('mandatory')
wfLnmInterfaceLrmCngstnErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfLnmInterfaceLrmCngstnErrs.setStatus('mandatory')
wfLnmInterfaceLrmRxErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfLnmInterfaceLrmRxErrors.setStatus('mandatory')
wfLnmInterfaceRemRxErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfLnmInterfaceRemRxErrors.setStatus('mandatory')
wfLnmInterfaceRpsRxErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfLnmInterfaceRpsRxErrors.setStatus('mandatory')
wfLnmInterfaceCrsRxErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfLnmInterfaceCrsRxErrors.setStatus('mandatory')
wfLnmInterfaceLbsRxErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfLnmInterfaceLbsRxErrors.setStatus('mandatory')
mibBuilder.exportSymbols("Wellfleet-LNM-MIB", wfLnmInterfaceLbsState=wfLnmInterfaceLbsState, wfLnmInterfaceDisable=wfLnmInterfaceDisable, wfLnmInterfaceOb3MgrPswd=wfLnmInterfaceOb3MgrPswd, wfLnmInterfaceRemState=wfLnmInterfaceRemState, wfLnmState=wfLnmState, wfLnmInterfaceRpsState=wfLnmInterfaceRpsState, wfLnmInterfaceRemoteMac=wfLnmInterfaceRemoteMac, wfLnmLnmSetsDisable=wfLnmLnmSetsDisable, wfLnmInterfaceCrsState=wfLnmInterfaceCrsState, wfLnmInterfaceCrsDisable=wfLnmInterfaceCrsDisable, wfLnmInterfaceOb2MgrPswd=wfLnmInterfaceOb2MgrPswd, wfLnmInterfaceOb2MgrMac=wfLnmInterfaceOb2MgrMac, wfLnmInterfaceOb1MgrPswd=wfLnmInterfaceOb1MgrPswd, wfLnmInterfaceRemDisable=wfLnmInterfaceRemDisable, wfLnmInterfaceCtrlMgrPswd=wfLnmInterfaceCtrlMgrPswd, wfLnmInterfaceRemRxErrors=wfLnmInterfaceRemRxErrors, wfLnmInterfaceDelete=wfLnmInterfaceDelete, wfLnmInterfaceLrmState=wfLnmInterfaceLrmState, wfLnmInterfaceEntry=wfLnmInterfaceEntry, wfLnmBridgeId=wfLnmBridgeId, wfLnmInterfaceLrmRxErrors=wfLnmInterfaceLrmRxErrors, wfLnmInterfaceOb1MgrMac=wfLnmInterfaceOb1MgrMac, wfLnmInternalLanId=wfLnmInternalLanId, wfLnmInterfaceMacCircuit=wfLnmInterfaceMacCircuit, wfLnmInterfaceRpsDisable=wfLnmInterfaceRpsDisable, wfLnmInterfaceCrsRxErrors=wfLnmInterfaceCrsRxErrors, wfLnmInterfaceCircuit=wfLnmInterfaceCircuit, wfLnmInterfaceRpsRxErrors=wfLnmInterfaceRpsRxErrors, wfLnmInterfaceWghtTrshld=wfLnmInterfaceWghtTrshld, wfLnmDisable=wfLnmDisable, wfLnmInterfaceCtrlMgrMac=wfLnmInterfaceCtrlMgrMac, wfLnmInterfaceLrmDisable=wfLnmInterfaceLrmDisable, wfLnm=wfLnm, wfLnmInterfaceLbsRxErrors=wfLnmInterfaceLbsRxErrors, wfLnmDelete=wfLnmDelete, wfLnmInterfaceLrmCngstnErrs=wfLnmInterfaceLrmCngstnErrs, wfLnmInterfaceOb3MgrMac=wfLnmInterfaceOb3MgrMac, wfLnmInterfaceTable=wfLnmInterfaceTable)
