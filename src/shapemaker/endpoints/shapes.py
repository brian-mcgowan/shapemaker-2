"""Enables public access to `Shape` functionality."""


from typing import List, Optional, Union
from uuid import UUID

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, Response, status

from shapemaker.containers import ApplicationContainer
from shapemaker.models.shape import Shape, ShapeCreateDTO, ShapeUpdateDTO
from shapemaker.services.shape import ShapeService
from shapemaker.utils.errors import NotFoundError


router = APIRouter(prefix="/shapes")


@router.post("/", response_model=Shape, status_code=status.HTTP_201_CREATED)
@inject
def create_shape(
    shape_dto: ShapeCreateDTO,
    shape_service: ShapeService = Depends(Provide[ApplicationContainer.shape_service]),
) -> Shape:
    """Creates a `Shape` resource and returns it to the client."""
    return shape_service.create(shape_dto)


@router.delete(
    "/{shape_id}", response_model=None, status_code=status.HTTP_204_NO_CONTENT
)
@inject
def delete_shape_by_id(
    shape_id: UUID,
    shape_service: ShapeService = Depends(Provide[ApplicationContainer.shape_service]),
) -> Optional[Response]:
    """Deletes a `Shape` resource."""
    try:
        shape_service.delete_by_id(shape_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@router.get("/{shape_id}", response_model=Shape, status_code=status.HTTP_200_OK)
@inject
def get_shape_by_id(
    shape_id: UUID,
    shape_service: ShapeService = Depends(Provide[ApplicationContainer.shape_service]),
) -> Union[Shape, Response]:
    """Retrieves a `Shape` resource and returns it to the client."""
    try:
        return shape_service.get_by_id(shape_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@router.get("/", response_model=List[Shape], status_code=status.HTTP_200_OK)
@inject
def get_shape_list(
    shape_service: ShapeService = Depends(Provide[ApplicationContainer.shape_service]),
) -> List[Shape]:
    """Retrieves all `Shape` resources and returns them to the client."""
    return shape_service.get_all()


@router.put("/{shape_id}", response_model=None, status_code=status.HTTP_200_OK)
@inject
def replace_by_id(
    shape_id: UUID,
    shape_dto: ShapeCreateDTO,
    shape_service: ShapeService = Depends(Provide[ApplicationContainer.shape_service]),
) -> Optional[Response]:
    """Replaces a `Shape` resource."""
    try:
        shape_service.replace_by_id(shape_id, shape_dto)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@router.patch("/{shape_id}", response_model=None, status_code=status.HTTP_200_OK)
@inject
def update_by_id(
    shape_id: UUID,
    shape_dto: ShapeUpdateDTO,
    shape_service: ShapeService = Depends(Provide[ApplicationContainer.shape_service]),
) -> Optional[Response]:
    """Partially updates a `Shape` resource."""
    try:
        shape_service.update_by_id(shape_id, shape_dto)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
