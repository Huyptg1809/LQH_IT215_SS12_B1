from sqlalchemy.orm import Session
from datetime import datetime
from fastapi import HTTPException, status
from models import DiscountModel

def delete_discount_service(discount_id: int, db: Session):

    discount = db.query(DiscountModel).filter(
        DiscountModel.id == discount_id,
        DiscountModel.is_deleted == False
    ).first()
    
    if not discount:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Mã giảm giá không tồn tại hoặc đã bị xóa"
        )
    
    if discount.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Không thể xóa mã giảm giá đang hoạt động"
        )
        
    discount.is_deleted = True
    discount.deleted_at = datetime.now()

    db.commit()
    
    return {"message": "Xóa mã giảm giá thành công", "discount_id": discount.id}
