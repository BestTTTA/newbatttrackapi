from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from bson import ObjectId


class SubStepDetail(BaseModel):
    completed: bool
    name: str
    time_start: str
    time_end: str
    
class SubStep1(BaseModel):
    ประกอบเซลล์โฮลเดอร์: SubStepDetail
    ติดอุปกรณ์ที่กล่องแบตเตอรรี่: SubStepDetail 
    ประกอบเซลล์แบตเตอรี่เข้ากับเซลล์โฮเดอร์: SubStepDetail 
    เจาะเตเปอร์บัสบาร์: SubStepDetail
    ประกอบ_BMS_and_Active_เข้าเพลทยึด: SubStepDetail
    ประกอบบอร์ดDry_Contact_เดินสาย_Comm_low_Comm_high: SubStepDetail
    ติดตั้งสาย_S: SubStepDetail
    QC_การเดินสายไฟ: SubStepDetail
    ประกอบลงกล่อง: SubStepDetail
    เดินสายขั้ว_บวก_ลบ: SubStepDetail
    เก็บสายไฟ: SubStepDetail
    QC_ความเรียบร้อยก่อนทดสอบ: SubStepDetail
    ตั้งค่า_BMS: SubStepDetail
    ชาร์จก่อนทดสอบ: SubStepDetail
    ทดสอบแบต: SubStepDetail
    ชาร์จหลังทดสอบ: SubStepDetail
    QC_ความเรียบร้อยก่อนปิดฝา: SubStepDetail
    ปิดฝากล่องแบตเตอรี่: SubStepDetail
    ติดสติ๊กเกอร์_S_N_วารันตี: SubStepDetail
class SubStep2(BaseModel):
    ติดอุปกรณ์หน้ากล่อง_Con_trol: SubStepDetail
    ติดตั้งเบรกเกอร์_400_A: SubStepDetail
    ติดตั้ง_คอนแทรคเตอร์: SubStepDetail
    ติดตั้งเทอมินอลหลังกล่อง: SubStepDetail
    ติดตั้งบอร์ด_Con_trol: SubStepDetail
    ติดตั้งชุดสายไฟ: SubStepDetail
    QC_ความเรียบร้อย_กล่อง_Con_trol: SubStepDetail
class SubStep3(BaseModel):
    บาลานซ์เซลล์_6Ah_32700: SubStepDetail
    สปอตแบตเตอรี่_แบตไฟเลี้ยงพัดลม_16S: SubStepDetail
    เดินสายไฟแบตเตอรี่_แบตไฟเลี้ยงพัดลม_16S: SubStepDetail
    ติดตั้ง_BMS_Active_สำหรับแบต_แบตไฟเลี้ยงพัดลม_16S: SubStepDetail
    QC_การเดินสายไฟแบตเตอรี่_แบตไฟเลี้ยงพัดลม_16S: SubStepDetail
    ตั้งค่า_BMS_แบตไฟเลี้ยงพัดลม_16S: SubStepDetail
    ทดสอบแบต_แบตไฟเลี้ยงพัดลม_16S: SubStepDetail
    QC_ความเรียบร้อย_แบตไฟเลี้ยงพัดลม_16S: SubStepDetail
    สปอตแบตเตอรี่_แบตไฟเลี้ยงพัดลม_8S: SubStepDetail
    ติดตั้งสาย_S_แบตไฟเลี้ยงพัดลม_8S:SubStepDetail
    ติดตั้ง_BMS_Active_สำหรับแบต_แบตไฟเลี้ยงพัดลม_8S: SubStepDetail
    QC_การเดินสายไฟแบตเตอรี่_แบตไฟเลี้ยงพัดลม_8S: SubStepDetail
    ตั้งค่า_BMS_แบตไฟเลี้ยงพัดลม_8S: SubStepDetail
    ทดสอบแบต_แบตไฟเลี้ยงพัดลม_8S: SubStepDetail
    QC_ความเรียบร้อย_แบตไฟเลี้ยงพัดลม_8S: SubStepDetail
    ติดตั้งเครื่องชาร์จ_48V_ที่กล่องแบตไฟเลี้ยงพัดลม: SubStepDetail
    ติดตั้งเครื่องชาร์จ_24V_ที่กล่องแบตไฟเลี้ยงพัดลม: SubStepDetail
    ติดตั้งปลั้กหน้าแปลนที่ก้นกล่องแบตไฟเลี้ยงพัดลม: SubStepDetail
    ตั้งค่าเครื่องชาร์จ_48V: SubStepDetail
    ตั้งค่าเครื่องชาร์จ_24V: SubStepDetail
    ทดสอบการใช้งานกล่องไฟเลี้ยงพัดลม: SubStepDetail
    QC_ความเรียบร้อยกล่องไฟเลี้ยงพัดลม: SubStepDetail 
class SubStep4(BaseModel):
    ประกอบแรค: SubStepDetail
    ติดตั้งกล่องControlที่แรค: SubStepDetail
    ติดตั้งกล่องไฟเลี้ยงระบบที่แรค: SubStepDetail
    ติดตั้งแบตเตอรี่ที่แรค: SubStepDetail
    เดินสายพัดลม: SubStepDetail
    เดินสายไฟ_ขั้ว_บวก_ขั้ว_ลบ: SubStepDetail
    ต่อสายอนุกรมหน้ากล่อง: SubStepDetail
    ต่อสายบาลานซ์หน้ากล่อง: SubStepDetail
    QC_ความเรียบร้อย: SubStepDetail
class SubStep5(BaseModel):
    ชาร์จก่อนทดสอบระบบ: SubStepDetail
    QC_ความเรียบร้อยก่อนทดสอบระบบ: SubStepDetail
    ทดสอบระบบ: SubStepDetail
    ชาร์จหลังทดสอบ: SubStepDetail 


class Step(BaseModel):
    id_step: str
    time_start: str
    time_end: str
    sub_steps1: SubStep1
    sub_steps2: SubStep2
    sub_steps3: SubStep3
    sub_steps4: SubStep4
    sub_steps5: SubStep5

class UpdateStepsModel(BaseModel):
    steps_to_update: List[str]
    
